
from django import forms
from .models import RegisteredUser, Company
from django.forms import ModelChoiceField

class SignUpForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    password = forms.CharField(widget=forms.PasswordInput())
    company = forms.ModelMultipleChoiceField(queryset=Company.objects.all(), widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = RegisteredUser
        fields = ['username', 'password', 'confirm_password', 'first_name', 'last_name', 'email', 'company']
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if RegisteredUser.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken.")
        return username

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput())
