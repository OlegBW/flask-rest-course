import os
from dotenv import load_dotenv
import requests

load_dotenv()


def send_mail(to: str, subject: str, body: str):
    return requests.post(
        "https://api.mailgun.net/v3/sandboxd351e28946b44e3992075c6f5d64af26.mailgun.org/messages",
        auth=("api", f"{os.getenv('MAILGUN_API_KEY')}"),
        data={
            "from": "OlegBW <mailgun@sandboxd351e28946b44e3992075c6f5d64af26.mailgun.org>",
            "to": [to],
            "subject": subject,
            "text": body,
        },
    )


def send_sign_up_mail(to: str):
    return send_mail(to, "Sign Up", "Succesful Sign Up!")
