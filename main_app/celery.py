import os
from datetime import timezone

from celery import Celery


# from .models import LoanApplication

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'loan_approval.settings')

app = Celery('loan_approval')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


# from .tasks import send_loan_approval_alert
#
# def approve_loan(request, loan_id):
#     loan = LoanApplication.objects.get(id=loan_id)
#     loan.approved = True
#     loan.approval_date = timezone.now()
#     loan.save()
#
#     # Trigger the Celery task
#     send_loan_approval_alert.delay(loan.id)
