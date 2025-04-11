from celery import shared_task
from .utils import send_loan_approval_email, send_loan_approval_sms

@shared_task
def send_loan_notifications(user_email, user_name, user_phone, loan_amount):
    send_loan_approval_email(user_email, user_name, loan_amount)
    send_loan_approval_sms(user_phone, user_name, loan_amount)

from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_loan_approval_alert(loan_id):
    from .models import LoanApplication
    loan = LoanApplication.objects.get(id=loan_id)
    send_mail(
        'Loan Approved',
        f'Your loan for {loan.amount} has been approved.',
        'langatenock231@gmail.com',
        [loan.applicant_email],
        fail_silently=False,
    )