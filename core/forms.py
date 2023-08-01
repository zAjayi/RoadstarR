from django import forms
from .models import UserInfo
from .models import ContactInfo
from django.forms import fields

class UserForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = '__all__'

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactInfo
        fields = '__all__'