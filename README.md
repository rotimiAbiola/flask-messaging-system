# Messaging System Application with Flask, RabbitMQ, Celery, and Nginx

## Overview

This application is a messaging system built using Flask, Celery, and RabbitMQ. It provides endpoints to queue email sending tasks and log messages to a file. The application also includes configurations for Celery and a bash script to set up the necessary system requirements on an Ubuntu/Debian-based OS.

## Files

1. `app.py`: Main Flask application with endpoints for adding tasks and logging.
2. `tasks.py`: Celery tasks for sending emails.
3. `celeryconfig.py`: Configuration file for Celery.
4. `nginx.conf`: Configuration file for Nginx.
5. `script.sh`: Bash script for installing system requirements and setting up the environment.

## Prerequisites

- Python 3.x
- RabbitMQ
- Nginx
- ngrok (for tunneling)
- Ubuntu/Debian-based OS

## Setup Instructions

If you have the prerequisites installed already, you can skip `step 2`.

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd <repository-directory>
```

### Step 2: Run Setup Script

```bash
chmod +x script.sh
./setup.sh
```

The `script.sh` script will:

- Install Python 3.x
- Install and configure RabbitMQ
- Install Nginx
- Install ngrok

### Step 3: Configure RabbitMQ

Edit the RabbitMQ credentials in `app.py`, `tasks.py`, and `celeryconfig.py` with your RabbitMQ user and password.

### Step 4: Configure SMTP Settings

Edit the SMTP settings in `tasks.py` with your SMTP server, port, sender email, and password.

### Step 5: Start Celery

Start up a celery in detached mode. This activates a celery worker in the background

```bash
celery -A app.celery worker --loglevel=info --detach
```

### Step 6: Start the Application

Activate the virtual environment and run the Flask application in the background.

```bash
python3 -m venv venv
source venv/bin/activate
nohup python app.py &
```

### Step 7: Configure Nginx

Copy the `nginx.conf` to the Nginx sites-available directory and create a symbolic link to sites-enabled.

```bash
sudo cp nginx.conf /etc/nginx/sites-available/messaging_system
sudo ln -s /etc/nginx/sites-available/messaging_system /etc/nginx/sites-enabled/
sudo service nginx restart
```

### Step 8: Start ngrok

Start ngrok to create a secure tunnel to the local server.

```bash
ngrok http 5000
```

This will provide a public URL that can be used to access the Flask application running on port 5000.

## Endpoints

### `GET /`

This endpoint triggers tasks based on query parameters.

- **Parameters:**

  - `sendmail`: Email address to send an email.
  - `talktome`: Any value to trigger logging.

- **Responses:**
  - 200: Task added to queue or log updated.
  - 400: Invalid request.

### `GET /logs`

This endpoint retrieves the log file contents.

- **Responses:**
  - 200: Log file contents.

## Logging

Logs are stored in `/var/log/messaging_system.log`. The `talktome` parameter in the root endpoint triggers a log entry with a timestamp.

## Email Sending

Emails are sent using the `send_email` task in `tasks.py`. The task is queued by Celery and executed asynchronously.

## Celery Configuration

Celery is configured in `celeryconfig.py` and integrated into the Flask application in `app.py`. The broker is RabbitMQ, and the result backend is RPC.

## Troubleshooting

- Ensure RabbitMQ and Nginx services are running.
- Check the log file at `/var/log/messaging_system.log` for any errors.
- Verify SMTP settings if emails are not being sent.
