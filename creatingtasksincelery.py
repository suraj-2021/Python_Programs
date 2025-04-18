from celery import shared_task

@shared_task
def process_data(data):
    # Time-consuming operation
    import time
    time.sleep(10)  # Simulate work
    return f"Processed: {data}"

@shared_task
def send_email(recipient, subject, message):
    # Email sending logic here
    print(f"Sending email to {recipient}")
    # ... email sending code
    return f"Email sent to {recipient}"
