from flask import Flask, render_template
from dotenv import load_dotenv
import os

# Create Flask application
app = Flask(__name__)

# Load environment variables
load_dotenv()

# Configuration
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.getenv('DB_USERNAME')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_DATABASE')}?charset=utf8mb4"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Import and register blueprints
from src.routes.messages import messages_bp
app.register_blueprint(messages_bp)

# Import database utility
from src.utils.db import db

# Routes
@app.route('/')
def index():
    """Main page route"""
    return render_template('index.html')

# Initialize database when the app is run directly
if __name__ == '__main__':
    # Import models here to avoid circular imports during testing
    from src.models.message import Message
    
    # Initialize database
    with app.app_context():
        db.init_app(app)
        db.create_all()
    
    app.run(debug=True, host='127.0.0.1', port=10000)
