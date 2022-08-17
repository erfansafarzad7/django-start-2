from django import forms
from .models import NewAccount

# Form For Add Account In AdminPanel
class NewAccountForm(forms.ModelForm):
    class Meta:
        model = NewAccount
        fields = ('name',)