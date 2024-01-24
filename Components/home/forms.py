from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError


class CustomUserCreationForm(forms.Form):
    firstname = forms.CharField(label='', min_length=4, max_length=20, widget=forms.TextInput(attrs={'class': "input-box fname" , 'value': 'Firstname'}))
    lastname = forms.CharField(label='', min_length=4, max_length=20, widget=forms.TextInput(attrs={'class': "input-box lname" , 'value': 'Lastname'}))
    gradelevel = forms.IntegerField(label="", widget=forms.TextInput(attrs={'class': "input-box grade"}))
    username = forms.CharField(label='', min_length=4, max_length=150, widget=forms.TextInput(attrs={'class': "input-box uname", 'value': 'Username'}))
    email = forms.EmailField(label='', widget=forms.TextInput(attrs={'class': "input-box email", 'value': 'Email'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': "input-box p1", 'value': 'Password1'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class': "input-box p2", 'value': 'Password2'}))

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Username already exists")
        return username

    def clean_firstname(self):
        firstname = self.cleaned_data['firstname']

        return firstname

    def clean_lastname(self):
        lastname = self.cleaned_data['lastname']

        return lastname

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1'],
            firstname = self.cleaned_data['firstname'],
            lastname = self.cleaned_data['lastname'],
            gradelevel = self.cleaned_data['gradelevel'],
        )
        return user