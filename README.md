# FastAPI Notification Service

A backend service built with FastAPI to manage and deliver notifications.

## Features
- CRUD APIs for notifications
- WebSocket support for real-time updates
- SQLAlchemy integration for database persistence
- Ready to extend with audit logs, queues, and personalization

## Getting Started
1. Clone the repo
2. Create a virtual environment
3. Install dependencies: `pip install -r requirements.txt`
4. Run the server: `uvicorn app.main:app --reload`

## Future Work
- Integration with Postgres
- AI-powered notification prioritization
- CI/CD with GitHub Actions