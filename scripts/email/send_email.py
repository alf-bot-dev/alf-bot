import smtplib
from email.message import EmailMessage
import json
import os

def send_email(subject, body, to_email):
    # Läs konfiguration från en lokal fil som *du* skapar (se README för stegen)
    config_path = os.path.expanduser("~/.alf-bot/email_config.json")
    
    if not os.path.exists(config_path):
        print(f"Konfigurationsfil saknas: {config_path}")
        return

    with open(config_path, 'r') as f:
        cfg = json.load(f)

    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = cfg['email']
    msg['To'] = to_email

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(cfg['email'], cfg['password'])
            smtp.send_message(msg)
        print("Mail skickat!")
    except Exception as e:
        print(f"Fel vid sändning: {e}")

if __name__ == "__main__":
    # Test-körning eller integration
    print("Email-modul redo.")
