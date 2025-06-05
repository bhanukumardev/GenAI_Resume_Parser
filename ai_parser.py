import json
import re
import requests
from config import Config

# --- OLLAMA LOCAL LLM SUPPORT ---
def query_ollama(prompt, model='llama3.2'):
    """Send prompt to local Ollama Llama 3.2 and return response text."""
    response = requests.post(
        'http://localhost:11434/api/generate',
        json={
            'model': model,
            'prompt': prompt,
            'stream': False
        }
    )
    return response.json()['response']

class AIResumeParser:
    def __init__(self):
        # Only initialize OpenAI if you have a key, otherwise use Ollama
        try:
            from openai import OpenAI
            self.openai_available = bool(Config.OPENAI_API_KEY)
            if self.openai_available:
                self.client = OpenAI(api_key=Config.OPENAI_API_KEY)
                self.openai_model = Config.OPENAI_MODEL
        except ImportError:
            self.openai_available = False

    def extract_resume_data(self, resume_text):
        prompt = self._create_extraction_prompt(resume_text)
        # Try OpenAI if available and you have credits
        if getattr(self, 'openai_available', False):
            try:
                response = self.client.chat.completions.create(
                    model=self.openai_model,
                    messages=[
                        {"role": "system", "content": "You are an expert resume parser. Extract information accurately and return valid JSON."},
                        {"role": "user", "content": prompt}
                    ],
                    max_tokens=1500,
                    temperature=0.1
                )
                extracted_data = response.choices[0].message.content
                return self._parse_response(extracted_data)
            except Exception as e:
                print(f"OpenAI failed: {e} - Falling back to Ollama.")
                # Fallback to Ollama
        # Always fallback to Ollama if OpenAI fails or is not available
        ollama_response = query_ollama(prompt, model='llama3.2')
        return self._parse_response(ollama_response)

    def _create_extraction_prompt(self, resume_text):
        return f"""
Extract the following information from this resume and return as valid JSON:

{{
    "personal_information": {{
        "name": "",
        "email": "",
        "phone": "",
        "address": ""
    }},
    "professional_summary": "",
    "skills": [],
    "work_experience": [
        {{
            "company": "",
            "position": "",
            "duration": "",
            "responsibilities": []
        }}
    ],
    "education": [
        {{
            "institution": "",
            "degree": "",
            "field": "",
            "year": ""
        }}
    ],
    "certifications": []
}}

Resume Text:
{resume_text}
"""

    def _parse_response(self, response_text):
        """Extract JSON from LLM response (handles code blocks and plain JSON)"""
        try:
            # Try to extract JSON between triple backticks (``````)
            match = re.search(r"``````", response_text, re.DOTALL)
            if match:
                json_str = match.group(1)
            else:
                # Fallback: find the first '{' and last '}'
                start = response_text.find('{')
                end = response_text.rfind('}')
                if start != -1 and end != -1 and end > start:
                    json_str = response_text[start:end+1]
                else:
                    raise Exception("Could not find JSON object in response.")
            return json.loads(json_str)
        except json.JSONDecodeError as e:
            raise Exception(f"Failed to parse AI response as JSON: {str(e)}\nResponse: {response_text}")

