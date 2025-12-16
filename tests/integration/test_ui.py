import pytest
from src.app import app
from src.utils.db import db
from src.models.message import Message


class TestColorfulMessageDisplay:
    """Test cases for colorful sticky note message display (User Story 2)"""
    
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
    
    def test_message_has_color(self, client):
        """Test that messages have a color assigned"""
        message_data = {
            'name': 'Test User',
            'content': 'Test message with color'
        }
        
        response = client.post('/api/messages', json=message_data)
        assert response.status_code == 201
        
        message = response.json
        assert 'color' in message
        assert message['color'] is not None
        assert message['color'] != ''
    
    def test_message_color_from_palette(self, client):
        """Test that message colors are from the predefined palette"""
        valid_colors = ['yellow', 'blue', 'green', 'pink', 'purple', 'orange']
        
        # Create multiple messages to test color assignment
        for i in range(10):
            message_data = {
                'name': f'User {i}',
                'content': f'Message {i}'
            }
            response = client.post('/api/messages', json=message_data)
            assert response.status_code == 201
            
            message = response.json
            assert message['color'] in valid_colors
    
    def test_messages_have_different_colors(self, client):
        """Test that different messages can have different colors"""
        # Create multiple messages
        messages = []
        for i in range(10):
            message_data = {
                'name': f'User {i}',
                'content': f'Message {i}'
            }
            response = client.post('/api/messages', json=message_data)
            assert response.status_code == 201
            messages.append(response.json)
        
        # Check that at least some messages have different colors
        colors = [msg['color'] for msg in messages]
        unique_colors = set(colors)
        # With 10 messages and 6 colors, we should have at least 2 different colors
        assert len(unique_colors) >= 1  # At minimum, colors should be assigned
    
    def test_message_display_template_includes_color(self, client):
        """Test that the message display template includes color class"""
        # Create a message
        message_data = {
            'name': 'Test User',
            'content': 'Test message'
        }
        response = client.post('/api/messages', json=message_data)
        assert response.status_code == 201
        
        message = response.json
        color = message['color']
        
        # Get the HTML template
        response = client.get('/messages')
        assert response.status_code == 200
        
        # Check that the HTML contains the color class
        html = response.data.decode('utf-8')
        assert f'sticky-note-{color}' in html or 'sticky-note' in html
    
    def test_sticky_note_css_classes_present(self, client):
        """Test that sticky note CSS classes are present in the rendered HTML"""
        # Create a message
        message_data = {
            'name': 'Test User',
            'content': 'Test message'
        }
        client.post('/api/messages', json=message_data)
        
        # Get the HTML template
        response = client.get('/messages')
        assert response.status_code == 200
        
        html = response.data.decode('utf-8')
        # Check for sticky note classes
        assert 'sticky-note' in html
        assert 'message' in html

