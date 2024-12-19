import smtplib
from email.message import EmailMessage

def send_email(subject, body, recipient):
    # Create an EmailMessage object
    msg = EmailMessage()

    # Set the subject
    msg['Subject'] = subject

    # Set the body
    msg.set_content(body)

    # Set the sender (you can customize this)
    msg['From'] = 'kiruthiga12.rajagopal@gmail.com'

    # Set the recipient
    msg['To'] = recipient

    try:
        # Connect to the SMTP server
        with smtplib.SMTP('smtp.gmail.com',587 ) as server:
            server.starttls()  # Start TLS encryption
            server.login('kiruthiga12.rajagopal@gmail.com', 'robcdscpdvkvmipk')  # Login to the SMTP server
            server.send_message(msg)  # Send the email
        print("hello")
    except Exception as e:
        print(f"An error occurred: {e}")

# Now you can call the send_email function with the appropriate parameters
send_email("Test Subject", "This is a test email message.", "yuvidiya12@gmail.com")
