from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from twilio.rest import Client


def send_loan_approval_email(user_email, user_name, loan_amount):
    subject = "Loan Approval Notification"
    message = render_to_string('loan_approved_email.html', {
        'user_name': user_name,
        'loan_amount': loan_amount
    })

    send_mail(subject, '', settings.DEFAULT_FROM_EMAIL, [user_email], html_message=message)


def send_loan_approval_sms(user_phone, user_name, loan_amount):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    message = f"Dear {user_name}, your loan of ${loan_amount} has been approved!"
    client.messages.create(body=message, from_=settings.TWILIO_PHONE_NUMBER, to=user_phone)
