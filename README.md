# Flask Messaging System with RabbitMQ, Celery, and Nginx

This project is a messaging system built with Flask, RabbitMQ, Celery, and Nginx. It allows sending emails and logging messages using a queue system for task management.

## Features

- **Email Sending**: Queue and send emails using RabbitMQ and Celery.
- **Logging**: Log messages with timestamps.
- **Nginx**: Serve the Flask application with Nginx.
- **Expose Locally with ngrok**: Make your local server accessible for external testing.

## Requirements

- Python 3.x
- RabbitMQ
- Nginx
- SMTP server credentials (e.g., Gmail)
- ngrok

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/repo-name.git
cd repo-name
```