from flask import Flask
from config import Config
from flask_cors import CORS

# Initialize the Flask app
app = Flask(__name__)

CORS(app)

from controllers.file_controller import file_bp
# Load configuration
app.config.from_object(Config)

# Register blueprints
app.register_blueprint(file_bp, url_prefix='/api/files')

if __name__ == '__main__':
    app.run(debug=True)
