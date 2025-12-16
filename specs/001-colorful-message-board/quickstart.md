# Quickstart: Colorful Message Board

**Feature**: Colorful Message Board
**Date**: 2025-12-16
**Branch**: 001-colorful-message-board

## Overview

This guide provides instructions for setting up, running, and testing the Colorful Message Board application.

## Prerequisites

- Python 3.11+
- Git
- Access to TiDB database (connection details provided in .env file)

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/dev-learn-hub/colorful-message-board.git
cd colorful-message-board
```

### 2. Checkout the Feature Branch

```bash
git checkout 001-colorful-message-board
```

### 3. Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

Create a `.env` file in the project root with the following content:

```env
DB_HOST=gateway01.ap-southeast-1.prod.aws.tidbcloud.com
DB_PORT=4000
DB_USERNAME='Zv6L2ZgnuM76GtJ.root'
DB_PASSWORD='7gsLIwXQwzO421FS'
DB_DATABASE='colorful_message_board'
```

## Running the Application

### Development Mode

```bash
flask run --debug
```

The application will be available at `http://localhost:5000`

### Production Mode

For production deployment on Vercel:

1. Install Vercel CLI:
   ```bash
   npm install -g vercel
   ```

2. Deploy to Vercel:
   ```bash
   vercel
   ```

Follow the prompts to configure your Vercel deployment.

## Testing

### Run Unit Tests

```bash
pytest tests/unit/
```

### Run Integration Tests

```bash
pytest tests/integration/
```

### Run All Tests

```bash
pytest
```

## Usage

1. Open your browser and navigate to the application URL
2. Enter your name and message in the input form at the top
3. Click "Submit" to post your message
4. Your message will appear in the message list with a colorful sticky note effect
5. New messages are displayed at the top of the list

## API Endpoints

### GET /messages
Retrieve all messages in reverse chronological order.

```bash
curl http://localhost:5000/messages
```

### POST /messages
Create a new message.

```bash
curl -X POST -H "Content-Type: application/json" -d '{"name": "John Doe", "content": "Hello, world!"}' http://localhost:5000/messages
```

### DELETE /messages/<id>
Delete a message by ID.

```bash
curl -X DELETE http://localhost:5000/messages/1
```

## Project Structure

```
src/
├── app.py              # Flask application entry point
├── models/             # Database models
│   └── message.py      # Message model
├── routes/             # API routes
│   └── messages.py     # Message routes
├── templates/          # HTML templates
│   └── index.html      # Main page template
├── static/             # Static files
│   ├── css/            # TailwindCSS output
│   └── js/             # HTMX and custom JavaScript
└── utils/              # Utility functions
    └── db.py           # Database connection

tests/
├── unit/               # Unit tests
│   └── test_message.py # Message model tests
└── integration/        # Integration tests
    └── test_api.py     # API integration tests

.env                    # Environment variables
requirements.txt        # Python dependencies
```

## Troubleshooting

### Database Connection Issues
- Verify that the environment variables in `.env` are correct
- Ensure that your IP address is whitelisted in the TiDB cloud console
- Check network connectivity to the TiDB server

### Application Won't Start
- Verify that all dependencies are installed correctly
- Check that the virtual environment is activated
- Look for error messages in the console output

### Messages Not Appearing
- Check that the database table exists (run migrations if needed)
- Verify that the form submission is working correctly
- Check browser developer tools for JavaScript errors

## Development Workflow

1. Create a new feature branch from `dev-iteration-1`
2. Write tests for the new feature
3. Implement the feature
4. Run tests to ensure they pass
5. Submit a pull request to `dev-iteration-1`
6. After review, merge into `dev-iteration-1`
