from flask import Blueprint, request, jsonify, render_template
from src.models.message import Message
from src.utils.db import db
from datetime import datetime

# Create blueprint
messages_bp = Blueprint('messages', __name__)

@messages_bp.route('/messages', methods=['GET'])
def get_messages():
    """Get all messages in reverse chronological order"""
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    return render_template('messages.html', messages=messages)

@messages_bp.route('/messages', methods=['POST'])
def create_message():
    """Create a new message"""
    try:
        if request.is_json:
            # JSON request (for API clients)
            data = request.get_json()
            name = data.get('name', '').strip()
            content = data.get('content', '').strip()
        else:
            # Form submission (for HTMX)
            name = request.form.get('name', '').strip()
            content = request.form.get('content', '').strip()
        
        # Validate input
        if not name:
            if request.is_json:
                return jsonify({'error': 'Name is required'}), 400
            else:
                return render_template('error.html', error='姓名不能为空'), 400
        
        if not content:
            if request.is_json:
                return jsonify({'error': 'Content is required'}), 400
            else:
                return render_template('error.html', error='留言内容不能为空'), 400
        
        # Validate length
        if len(name) > 255:
            if request.is_json:
                return jsonify({'error': 'Name must be 255 characters or less'}), 400
            else:
                return render_template('error.html', error='姓名不能超过255个字符'), 400
        
        if len(content) > 1000:
            if request.is_json:
                return jsonify({'error': 'Content must be 1000 characters or less'}), 400
            else:
                return render_template('error.html', error='留言内容不能超过1000个字符'), 400
        
        # Create new message
        message = Message(name=name, content=content)
        db.session.add(message)
        db.session.commit()
        
        if request.is_json:
            # Return JSON response for API clients
            return jsonify(message.to_dict()), 201
        else:
            # Return HTML for HTMX
            return render_template('messages.html', messages=Message.query.order_by(Message.timestamp.desc()).all())
    
    except Exception as e:
        db.session.rollback()
        if request.is_json:
            return jsonify({'error': 'An error occurred while creating the message'}), 500
        else:
            return render_template('error.html', error='创建留言时发生错误'), 500

@messages_bp.route('/api/messages', methods=['GET'])
def api_get_messages():
    """API endpoint to get all messages as JSON"""
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    return jsonify([message.to_dict() for message in messages])

@messages_bp.route('/api/messages', methods=['POST'])
def api_create_message():
    """API endpoint to create a new message"""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Request body is required'}), 400
        
        name = data.get('name', '').strip()
        content = data.get('content', '').strip()
        
        # Validate input
        if not name:
            return jsonify({'error': 'Name is required'}), 400
        
        if not content:
            return jsonify({'error': 'Content is required'}), 400
        
        # Validate length
        if len(name) > 255:
            return jsonify({'error': 'Name must be 255 characters or less'}), 400
        
        if len(content) > 1000:
            return jsonify({'error': 'Content must be 1000 characters or less'}), 400
        
        # Create new message
        message = Message(name=name, content=content)
        db.session.add(message)
        db.session.commit()
        
        return jsonify(message.to_dict()), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'An error occurred while creating the message'}), 500
