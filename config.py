import os

class Config:
    # Directory for file uploads
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
    OUTPUT_FOLDER = os.path.join(os.getcwd(), 'output')
    
    # Ensure the folders exist
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    
    # Maximum file upload size (16MB in this case)
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024

    # Allowed extensions
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'txt', 'doc', 'docx'}
