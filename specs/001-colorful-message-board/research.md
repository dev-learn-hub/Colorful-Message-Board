# Research: Colorful Message Board

**Feature**: Colorful Message Board
**Date**: 2025-12-16
**Branch**: 001-colorful-message-board

## Decisions & Rationale

### Technology Stack

| Decision | Rationale | Alternatives Considered |
|----------|-----------|-------------------------|
| **Backend**: Flask | Lightweight, well-documented Python framework suitable for web applications. Ideal for the pure backend architecture requirement. | FastAPI, Django |
| **Frontend**: HTMX + TailwindCSS | HTMX allows for dynamic UI updates without heavy frontend frameworks, aligning with pure backend approach. TailwindCSS provides rapid styling for the colorful sticky note effect. | React, Vue, plain CSS |
| **Testing**: pytest | Standard Python testing framework with extensive ecosystem support. | unittest, nose |
| **Database**: TiDB | Provided by the user with connection details. Distributed SQL database with MySQL compatibility. | PostgreSQL, SQLite |
| **Deployment**: Vercel | Serverless platform suitable for Flask applications with easy deployment process. | AWS Lambda, Heroku |

### Architecture

| Decision | Rationale | Alternatives Considered |
|----------|-----------|-------------------------|
| **Integrated Frontend-Backend Structure** | Combines Flask backend with HTMX/TailwindCSS frontend in a single codebase, following the pure backend architecture requirement while allowing for dynamic UI. | Separate frontend-backend repositories |
| **Vertical Mobile Layout** | Designed specifically for mobile devices with vertical scrolling, input at top, and messages below. | Responsive layout for both desktop and mobile |
| **Reverse Chronological Message Order** | Displays newest messages at the top, which is intuitive for users viewing recent content. | Chronological order |
| **Colorful Sticky Note Visual Effect** | Enhances user experience with visually appealing design, using CSS styles to create sticky note appearance with random colors. | Simple text messages, uniform styling |

## Implementation Details

### Database Model

- **Message** entity with attributes: id, name, content, timestamp, color
- TiDB database connection using SQLAlchemy ORM

### API Endpoints

- GET /messages - Retrieve all messages
- POST /messages - Create a new message
- DELETE /messages/<id> - Delete a message (future enhancement)

### UI Components

- Message input form at top of screen
- Message list with colorful sticky note styling
- HTMX for dynamic message updates without page refresh

## Dependencies

### Python
- Flask
- SQLAlchemy
- python-dotenv
- requests (for testing)

### Frontend
- HTMX
- TailwindCSS

### Development Tools
- pytest
- black (code formatting)
- flake8 (linting)
