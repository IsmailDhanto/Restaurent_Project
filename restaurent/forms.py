from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from .models import *


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control form-floating mb-3"}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control form-floating mb-3"})
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control form-floating mb-3"}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control form-floating mb-3"})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control form-floating mb-3"})
    )
    email = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control form-floating mb-3"}))
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "password1",
            "password2",
            "is_admin",
            "is_cashier",
            "is_waiter",
        )

class FormProduct(ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class  Trans_form(ModelForm):
    class Meta:
        model = Transaction
        fields = ['payment_status']