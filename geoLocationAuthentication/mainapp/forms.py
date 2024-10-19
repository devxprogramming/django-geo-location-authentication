from django import forms
from django.forms import ModelForm
from .models import User, UserSession
from django.contrib.auth.forms import UserCreationForm
class UserForm(UserCreationForm):
    ip_address = forms.CharField(widget=forms.HiddenInput(), required=False)
    longitude = forms.FloatField(widget=forms.HiddenInput(), required=False)
    latitude = forms.FloatField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'ip_address', 'longitude', 'latitude']
        widgets = {
            'ip_address': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
            'latitude': forms.HiddenInput(),
        }
        