from django import forms
from main_app.models import LoanApplication

LOAN_PURPOSE_CHOICES = {
    "Education": "Education",
    "Business": "Business",
    "Medical": "Medical",
    "Personal": "Personal"
}

class LoanApplicationForm(forms.ModelForm):
    loan_purpose = forms.ChoiceField(choices=LOAN_PURPOSE_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = LoanApplication
        fields = ['customer', 'amount', 'loan_term', 'loan_purpose', 'application_date']
        widgets = {
            'amount': forms.NumberInput(attrs={'type': 'number', 'min': '1000', 'max': '1000000'}),
            'loan_term': forms.NumberInput(attrs={'type': 'number', 'min': '1', 'max': '60'}),  # months
            'application_date': forms.DateInput(attrs={'type': 'date'}),
        }
