import base64
from flask import Blueprint, request, send_file, jsonify, current_app
from werkzeug.utils import secure_filename
import os
from services.file_service import convert_file_to_pdf

file_bp = Blueprint('file_bp', __name__)

# Allowed file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'txt', 'doc', 'docx'}

def allowed_file(filename):
    """Check if the uploaded file is allowed based on its extension"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@file_bp.route('/app',methods=['GET'])
def hello_ap():
    return jsonify({'message': 'Hello There! Pdf service up now'}), 200

@file_bp.route('/convert', methods=['POST'])
def upload_file():
    """
    API Endpoint: /api/files/convert
    Accepts a file via POST, converts it to PDF, and returns the generated PDF file.
    """
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        upload_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file.save(upload_path)
        
        # Convert file to PDF
        pdf_path = convert_file_to_pdf(upload_path, filename)

        if pdf_path:
            # Read PDF data and encode it in Base64
            with open(pdf_path, "rb") as pdf_file:
                pdf_data = pdf_file.read()
                pdf_base64 = base64.b64encode(pdf_data).decode('utf-8')  # Encode to Base64

            # Return JSON response with the PDF data
            return jsonify({'pdf_data': pdf_base64}), 200
        else:
            return jsonify({'error': 'File conversion failed'}), 500

    return jsonify({'error': 'File type not allowed'}), 400
