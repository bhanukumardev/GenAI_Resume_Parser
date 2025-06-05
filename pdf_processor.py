import PyPDF2
import io
from werkzeug.utils import secure_filename

class PDFProcessor:
    
    @staticmethod
    def extract_text_from_pdf(file_stream):
        """Extract text from uploaded PDF file"""
        try:
            pdf_reader = PyPDF2.PdfReader(file_stream)
            text = ""
            
            for page in pdf_reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
            
            return text.strip()
        except Exception as e:
            raise Exception(f"Error extracting text from PDF: {str(e)}")
    
    @staticmethod
    def validate_file(file):
        """Validate uploaded file"""
        if not file or file.filename == '':
            return False, "No file selected"
        
        if not file.filename.lower().endswith('.pdf'):
            return False, "Only PDF files are supported"
        
        return True, "File is valid"
