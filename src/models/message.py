from datetime import datetime, timezone
import random
from src.utils.db import db

class Message(db.Model):
    """Message model representing a single message on the board"""
    
    # Table name
    __tablename__ = 'messages'
    
    # Predefined color palette
    COLORS = ['yellow', 'blue', 'green', 'pink', 'purple', 'orange']
    
    # Columns
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=lambda: datetime.now(timezone.utc))
    color = db.Column(db.String(20), nullable=False)
    
    def __init__(self, name, content):
        """Initialize a new Message instance with a random color"""
        self.name = name
        self.content = content
        self.timestamp = datetime.now(timezone.utc)
        self.color = random.choice(self.COLORS)
    
    def __repr__(self):
        """String representation of the Message"""
        return f'<Message {self.id} - {self.name}: {self.content[:20]}...>'
    
    def to_dict(self):
        """Convert the Message to a dictionary for JSON serialization"""
        return {
            'id': self.id,
            'name': self.name,
            'content': self.content,
            'timestamp': self.timestamp.isoformat(),
            'color': self.color
        }
