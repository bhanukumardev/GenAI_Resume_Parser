# 🤖 GenAI Resume Parser

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/bhanukumardev/GenAI_Resume_Parser)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![OpenAI](https://img.shields.io/badge/OpenAI-412991?logo=openai&logoColor=white)](https://openai.com/)
[![Ollama](https://img.shields.io/badge/Ollama-Local%20AI-orange)](https://ollama.ai/)
[![Stars](https://img.shields.io/github/stars/bhanukumardev/GenAI_Resume_Parser?style=social)](https://github.com/bhanukumardev/GenAI_Resume_Parser/stargazers)

> AI-powered resume parser using Flask, OpenAI, and Ollama — Extract structured insights from PDF resumes with hybrid cloud/local AI.

## 📹 Demo

**[📺 Watch Video Demo on LinkedIn →](https://www.linkedin.com/posts/bhanu-kumar-dev-97b820313_pinnaclelabs-genai-ai-activity-7334604534679302144-WLN8?utm_source=share&utm_medium=member_desktop)**

## 🚀 Overview

A cutting-edge resume parsing solution that leverages **Generative AI** to extract structured information from PDF resumes. Built as part of Pinnacle Labs Internship, this project demonstrates:

- **Hybrid AI Approach** - Use OpenAI API or local Llama 3.2 via Ollama
- **Intelligent Parsing** - Extracts name, email, skills, experience, education
- **Flexible Deployment** - Cloud or on-premises AI models
- **Simple Interface** - Clean Flask web application

## ✨ Features

- 📄 **PDF Resume Upload** - Drag & drop or select files
- 🤖 **AI Extraction** - Intelligent parsing using LLMs
- 🌐 **Hybrid AI Models**
  - ☁️ OpenAI GPT-4 / GPT-3.5 (Cloud)
  - 💻 Llama 3.2 via Ollama (Local)
- 📊 **Structured Output** - JSON format with key resume fields
- ⚡ **Fast Processing** - Optimized for quick results
- 🔒 **Privacy Options** - Keep data local with Ollama

## 🛠️ Tech Stack

### Backend
- **Framework:** Flask (Python)
- **PDF Processing:** PyPDF2 / pdfplumber
- **AI Models:**
  - OpenAI API (GPT-4, GPT-3.5-turbo)
  - Ollama (Llama 3.2 local deployment)

### Frontend
- **HTML/CSS/JavaScript**
- **Bootstrap** for responsive design
- **AJAX** for async file uploads

### AI Integration
- **LangChain** - AI orchestration
- **Prompt Engineering** - Optimized extraction prompts
- **Error Handling** - Robust fallback mechanisms

## 📦 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager
- (Optional) OpenAI API key
- (Optional) Ollama installed locally

### 1. Clone Repository

```bash
git clone https://github.com/bhanukumardev/GenAI_Resume_Parser.git
cd GenAI_Resume_Parser
```

### 2. Install Dependencies

```bash
# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required packages
pip install -r requirements.txt
```

### 3. Configure AI Models

#### Option A: OpenAI (Cloud)

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key_here
MODEL_TYPE=openai
```

#### Option B: Ollama (Local)

```bash
# Install Ollama (if not already installed)
# Visit: https://ollama.ai/download

# Pull Llama 3.2 model
ollama pull llama3.2

# Start Ollama server
ollama serve
```

Create a `.env` file:

```env
MODEL_TYPE=ollama
OLLAMA_MODEL=llama3.2
```

### 4. Run the Application

```bash
# Start Flask app
python app.py

# Access at http://localhost:8000
```

## 🎯 Usage Example

### Web Interface

1. Open `http://localhost:8000` in your browser
2. Upload a PDF resume
3. Click "Parse Resume"
4. View extracted information in structured JSON format

### API Usage

```python
import requests

# Upload and parse resume
with open('resume.pdf', 'rb') as f:
    files = {'file': f}
    response = requests.post('http://localhost:8000/parse', files=files)
    
resume_data = response.json()
print(resume_data)
```

### Example Output

```json
{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "phone": "+1-234-567-8900",
  "skills": ["Python", "Machine Learning", "Flask", "AI"],
  "experience": [
    {
      "company": "Tech Corp",
      "position": "Software Engineer",
      "duration": "2020-2023"
    }
  ],
  "education": [
    {
      "degree": "B.Tech in Computer Science",
      "institution": "University Name",
      "year": "2020"
    }
  ]
}
```

## 📊 Supported Fields

- 👤 Personal Information (Name, Email, Phone, LinkedIn)
- 🎓 Education (Degree, Institution, Year, GPA)
- 💼 Work Experience (Company, Role, Duration, Responsibilities)
- 🛠️ Technical Skills (Programming, Tools, Frameworks)
- 🏆 Certifications and Awards
- 📋 Projects and Publications

## 📁 Project Structure

```
GenAI_Resume_Parser/
├── app.py                  # Main Flask application
├── parser/                 # Resume parsing logic
│   ├── openai_parser.py    # OpenAI integration
│   └── ollama_parser.py    # Ollama integration
├── templates/              # HTML templates
├── static/                 # CSS, JS, images
├── uploads/                # Temporary resume storage
├── requirements.txt        # Python dependencies
├── .env.example            # Environment variables template
└── README.md               # Project documentation
```

## 🔒 Privacy & Security

- **Local Processing:** Use Ollama to keep all data on-premises
- **No Data Storage:** Uploaded resumes are processed and deleted
- **Secure API Keys:** Environment variables for credentials
- **GDPR Compliant:** No personal data retention

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/NewFeature`)
3. Commit your changes (`git commit -m 'Add NewFeature'`)
4. Push to the branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Bhanu Kumar Dev**
- 🎓 3rd Year CSSE @ KIIT University
- 👨‍💻 Pinnacle Labs Intern | AI/ML Developer
- 📧 Email: kumarbhanu818@gmail.com
- 💼 LinkedIn: [bhanu-kumar-dev-97b820313](https://www.linkedin.com/in/bhanu-kumar-dev-97b820313)
- 🐙 GitHub: [@bhanukumardev](https://github.com/bhanukumardev)
- 🌐 Portfolio: [bhanukumardev.github.io/bhanu-portfolio](https://bhanukumardev.github.io/bhanu-portfolio/)

## 🌟 Acknowledgments

- **Pinnacle Labs** - For the internship opportunity
- **OpenAI** - For powerful GPT models
- **Ollama Team** - For local AI deployment tools
- **Flask Community** - For excellent documentation

## 📈 Future Enhancements

- [ ] Support for DOCX and other formats
- [ ] Batch processing capabilities
- [ ] Advanced resume scoring
- [ ] Integration with ATS systems
- [ ] Multi-language support
- [ ] Resume comparison features

---

<div align="center">
  <b>⭐ Star this repo if you find it helpful!</b>
  <br>
  <i>Empowering recruitment with AI-driven insights</i>
  <br>
  Made with ❤️ by Bhanu Kumar Dev | Pinnacle Labs Internship Project
</div>
