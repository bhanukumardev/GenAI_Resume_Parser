from flask import Flask, render_template, request, jsonify
from pdf_processor import PDFProcessor
from ai_parser import AIResumeParser
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

pdf_processor = PDFProcessor()
ai_parser = AIResumeParser()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/parse', methods=['POST'])
def parse_resume():
    try:
        if 'resume_file' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400

        file = request.files['resume_file']
        is_valid, message = pdf_processor.validate_file(file)
        if not is_valid:
            return jsonify({'error': message}), 400

        resume_text = pdf_processor.extract_text_from_pdf(file)
        if not resume_text.strip():
            return jsonify({'error': 'No text found in PDF'}), 400

        extracted_data = ai_parser.extract_resume_data(resume_text)
        return jsonify({
            'success': True,
            'data': extracted_data,
            'raw_text': resume_text[:500] + '...' if len(resume_text) > 500 else resume_text
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health')
def health_check():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
