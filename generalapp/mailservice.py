""" 
Code for sending email to google account using api key from app.Brevo.com,
by sendin a post request to this url: https://api.mailersend.com/v3/smtp/email
Python configuration for sending the mail through mailserder

"""
import requests
#from . import models

# MAIL_API = 'https://api.brevo.com/v3/emailCampaigns'
api_key = ""


def send_mail(recipient_email, mail_info, mail_subj, std_name):
    # Brevo API endpoint for sending transactional emails..
    url = 'https://api.brevo.com/v3/smtp/email'

    # The email data we are sending to the user..
    payload = {
        "sender": {
            "name": f"Flare Network",
            "email": "pinetwork@sidratrade.info"
        },
        "to": [
            {
                "email": recipient_email,
                "name": f"{std_name}"
            }
        ],
        "subject": f"{mail_subj}",
        "htmlContent": f"{mail_info}"
    }

    # Our authorization header..
    headers = {
        'api-key': api_key,
        'Content-Type': 'application/json',
        'accept': 'application/json',
    }

    # Our post request..
    response = requests.post(url, json=payload, headers=headers)
    return

