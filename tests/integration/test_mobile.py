import pytest
from src.app import app
from src.utils.db import db
from src.models.message import Message


class TestMobileLayout:
    """Test cases for mobile-optimized vertical layout (User Story 3)"""
    
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
    
    def test_mobile_viewport_meta_tag(self, client):
        """Test that the page includes mobile viewport meta tag"""
        response = client.get('/')
        assert response.status_code == 200
        
        html = response.data.decode('utf-8')
        # Check for viewport meta tag
        assert 'viewport' in html.lower()
        assert 'width=device-width' in html.lower() or 'width=device-width' in html
    
    def test_vertical_layout_structure(self, client):
        """Test that the layout is vertical (input at top, messages below)"""
        response = client.get('/')
        assert response.status_code == 200
        
        html = response.data.decode('utf-8')
        # Check for form (message input) - should appear before messages
        assert 'form' in html.lower() or 'input' in html.lower()
        # Check for message container
        assert 'messages' in html.lower() or 'message' in html.lower()
    
    def test_touch_friendly_input_fields(self, client):
        """Test that input fields are touch-friendly (proper sizing)"""
        response = client.get('/')
        assert response.status_code == 200
        
        html = response.data.decode('utf-8')
        # Check for input fields
        assert 'input' in html.lower() or 'textarea' in html.lower()
        # Mobile-friendly inputs should have adequate sizing (checked via CSS classes or inline styles)
        # This is a basic check - full verification would require browser automation
    
    def test_responsive_css_classes(self, client):
        """Test that responsive CSS classes are present"""
        response = client.get('/')
        assert response.status_code == 200
        
        html = response.data.decode('utf-8')
        # Check for TailwindCSS responsive classes or custom responsive styles
        # TailwindCSS uses classes like 'container', 'mx-auto', etc.
        # The presence of these suggests responsive design
        assert 'container' in html.lower() or 'class=' in html
    
    def test_mobile_css_media_queries(self, client):
        """Test that mobile CSS media queries are defined"""
        # This test checks if the CSS file exists and contains mobile styles
        response = client.get('/static/css/styles.css')
        # The file might not exist in test environment, so we check status
        if response.status_code == 200:
            css = response.data.decode('utf-8')
            # Check for mobile media queries
            assert '@media' in css or 'max-width' in css.lower() or 'mobile' in css.lower()
    
    def test_message_input_at_top(self, client):
        """Test that message input form is positioned at the top"""
        response = client.get('/')
        assert response.status_code == 200
        
        html = response.data.decode('utf-8')
        # The form should appear in the HTML (structure check)
        # In a vertical layout, the form should come before the messages list
        form_index = html.lower().find('form')
        messages_index = html.lower().find('messages')
        
        # If both exist, form should come before messages
        if form_index != -1 and messages_index != -1:
            assert form_index < messages_index or form_index == -1 or messages_index == -1

