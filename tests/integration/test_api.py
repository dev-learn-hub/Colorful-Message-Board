import pytest
from src.app import app
from src.utils.db import db
from src.models.message import Message

class TestMessageAPI:
    """Test cases for the Message API endpoints"""
    
    @pytest.fixture
    def client(self):
        """Create and configure a test client"""
        # Save original configuration to restore later
        original_db_uri = app.config.get('SQLALCHEMY_DATABASE_URI')
        original_testing = app.config.get('TESTING')
        
        # Set test configuration
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        
        # Import models here to avoid circular imports
        from src.models.message import Message
        
        with app.test_client() as client:
            with app.app_context():
                # Initialize database if not already initialized
                if 'sqlalchemy' not in app.extensions:
                    db.init_app(app)
                
                # Create all tables
                db.create_all()
                
                # Clear any existing data
                db.session.query(Message).delete()
                db.session.commit()
            
            yield client
            
        # Restore original configuration
        app.config['SQLALCHEMY_DATABASE_URI'] = original_db_uri
        app.config['TESTING'] = original_testing
            
    def test_get_messages(self, client):
        """Test that GET /api/messages returns an empty list initially"""
        response = client.get('/api/messages')
        assert response.status_code == 200
        assert response.json == []
    
    def test_create_message(self, client):
        """Test that POST /api/messages creates a new message"""
        message_data = {
            'name': 'Test User',
            'content': 'Test message'
        }
        
        response = client.post('/api/messages', json=message_data)
        assert response.status_code == 201
        
        # Check that the message was created
        response = client.get('/api/messages')
        assert len(response.json) == 1
        assert response.json[0]['name'] == 'Test User'
        assert response.json[0]['content'] == 'Test message'
        assert response.json[0]['color'] is not None
    
    def test_create_message_without_name(self, client):
        """Test that POST /api/messages requires a name"""
        message_data = {
            'content': 'Test message without name'
        }
        
        response = client.post('/api/messages', json=message_data)
        assert response.status_code == 400
    
    def test_create_message_without_content(self, client):
        """Test that POST /api/messages requires content"""
        message_data = {
            'name': 'Test User'
        }
        
        response = client.post('/api/messages', json=message_data)
        assert response.status_code == 400
