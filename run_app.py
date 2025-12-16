#!/usr/bin/env python
"""Temporary script to run the app with test database for UI verification"""
from src.app import app
from src.utils.db import db
from src.models.message import Message

# Use SQLite for testing
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['TESTING'] = False

# Initialize database
with app.app_context():
    db.init_app(app)
    db.create_all()
    print("Database initialized")

if __name__ == '__main__':
    print("Starting Flask app on http://127.0.0.1:10000")
    app.run(debug=True, host='127.0.0.1', port=10000, use_reloader=False)

