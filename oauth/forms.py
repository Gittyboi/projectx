from django import forms
from oauth.models import Customer


class CustomerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Customer
        fields = ['username', 'email', 'password']
