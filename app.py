from flask import Flask, request, jsonify
from celery import Celery
import logging
from datetime import datetime
from tasks import send_email

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'amqp://<RABBITMQ-USER>:<RABBITMQ-PASSWORD>@localhost//'
app.config['CELERY_RESULT_BACKEND'] = 'rpc://'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

@celery.task
def send_email_task(recipient):
    return send_email(recipient)

@app.route('/', methods=['GET'])
def endpoint():
    sendmail = request.args.get('sendmail')
    talktome = request.args.get('talktome')

    if sendmail:
        send_email.apply_async(args=[sendmail])
        return jsonify({"status": "Email task added to queue"}), 200

    if talktome:
        log_message = f"{datetime.now()} - Talk to me triggered\n"
        with open("/var/log/messaging_system.log", "a") as log_file:
            log_file.write(log_message)
        return jsonify({"status": "Log updated"}), 200

    return jsonify({"error": "Invalid request"}), 400
@app.route('/logs', methods=['GET'])
def logs():
    with open("/var/log/messaging_system.log", "r") as log_file:
        logs = log_file.read()
    return logs, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)