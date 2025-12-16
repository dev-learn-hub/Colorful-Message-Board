# Data Model: Colorful Message Board

**Feature**: Colorful Message Board
**Date**: 2025-12-16
**Branch**: 001-colorful-message-board

## Overview

The data model defines the structure of data entities for the Colorful Message Board application. The primary entity is `Message`, which represents a single message posted on the board with a colorful sticky note visual effect.

## Entities

### Message

| Field Name | Type | Description | Constraints |
|------------|------|-------------|-------------|
| `id` | Integer | Unique identifier for the message | Primary key, auto-increment |
| `name` | String (255) | Name of the message author | Required, non-empty |
| `content` | Text | Content of the message | Required, non-empty |
| `timestamp` | DateTime | When the message was created | Required, default to current time |
| `color` | String (20) | Color assigned to the message | Required, one of predefined color palette |

## Relationships

- The Message entity has no relationships with other entities in the initial version

## Validation Rules

- `name`: Must be between 1 and 255 characters
- `content`: Must be between 1 and 1000 characters
- `color`: Must be one of the predefined colors: 'yellow', 'blue', 'green', 'pink', 'purple', 'orange'
- `timestamp`: Must be a valid datetime value, defaults to current UTC time

## Data Flow

1. User submits a new message through the web interface
2. Server validates the input data
3. System assigns a random color from the predefined palette
4. Message is stored in the TiDB database with current timestamp
5. Message appears in the message list in reverse chronological order

## Database Schema

```sql
CREATE TABLE messages (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    timestamp DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    color VARCHAR(20) NOT NULL
);
```

## ORM Mapping

The Message entity will be mapped using SQLAlchemy ORM with the following structure:

```python
class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    color = db.Column(db.String(20), nullable=False)
```

## Color Palette

The application will use the following predefined color palette for messages:

- yellow
- blue
- green
- pink
- purple
- orange

These colors will be mapped to CSS classes to create the colorful sticky note visual effect.
