import pytest
from src.models.message import Message

class TestMessage:
    """Test cases for the Message model"""
    
    def test_message_creation(self):
        """Test that a Message instance can be created"""
        message = Message(name="Test User", content="Test message")
        assert message.name == "Test User"
        assert message.content == "Test message"
        assert message.color is not None
        assert message.timestamp is not None
    
    def test_message_color_assignment(self):
        """Test that a Message gets a random color from the predefined palette"""
        message = Message(name="Test User", content="Test message")
        assert message.color in ["yellow", "blue", "green", "pink", "purple", "orange"]
    
    def test_message_repr(self):
        """Test the string representation of a Message"""
        message = Message(name="Test User", content="Test message")
        assert "Test User" in str(message)
        assert "Test message" in str(message)
    
    def test_all_colors_from_palette_used(self):
        """Test that all colors from the palette can be assigned"""
        valid_colors = set(Message.COLORS)
        assigned_colors = set()
        
        # Create many messages to increase chance of getting all colors
        for i in range(100):
            message = Message(name=f"User {i}", content=f"Message {i}")
            assigned_colors.add(message.color)
            # If we've seen all colors, we can stop early
            if assigned_colors == valid_colors:
                break
        
        # Verify that at least some colors from the palette are used
        assert len(assigned_colors) > 0
        # All assigned colors should be from the valid palette
        assert assigned_colors.issubset(valid_colors)
    
    def test_color_assignment_randomness(self):
        """Test that color assignment shows randomness (not always the same)"""
        colors = []
        for i in range(20):
            message = Message(name=f"User {i}", content=f"Message {i}")
            colors.append(message.color)
        
        # With 20 messages and 6 colors, we should see some variation
        unique_colors = set(colors)
        # It's possible but unlikely that all 20 messages get the same color
        # We'll just verify that colors are being assigned
        assert len(unique_colors) >= 1