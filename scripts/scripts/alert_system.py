import smtplib
from email.mime.text import MIMEText

def send_alert(recipient, subject, body):
    sender = "your_email@example.com"
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    try:
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login(sender, "your_password")
            server.sendmail(sender, [recipient], msg.as_string())
            print(f"Alert sent to {recipient}")
    except Exception as e:
        print(f"Failed to send alert: {e}")

if __name__ == "__main__":
    # Example alert message
    send_alert("recipient@example.com", "Transaction Alert", "Suspicious transaction detected.")
