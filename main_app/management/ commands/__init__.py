# your_app/management/commands/import_fake_data.py

from django.core.management.base import BaseCommand
from your_app.models import LoanApplication


class Command(BaseCommand):
    help = 'Imports fake loan application data into the database.'

    def handle(self, *args, **kwargs):
        # Fake loan data as example
        loan_data = [
            {
                "name": "Megan Ruiz",
                "ID_no": "716-55-5521",
                "email": "greerkatie@hotmail.com",
                "amount": 22113,
                "status": "Rejected"
            },
            {
                "name": "Steven Ochoa",
                "ID_no": "596-51-8552",
                "email": "oalexander@lloyd-bell.org",
                "amount": 43684,
                "status": "Rejected"
            },
            # Add more fake data here...
        ]

        for data in loan_data:
            # Create LoanApplication objects from the fake data
            LoanApplication.objects.create(
                name=data['name'],
                ID_no=data['ID_no'],
                email=data['email'],
                amount=data['amount'],
                status=data['status']
            )

        self.stdout.write(self.style.SUCCESS('Successfully imported fake loan data'))
