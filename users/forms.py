from django import forms
from django.contrib.auth.models import User
from bootstrap_toolkit.widgets import BootstrapTextInput

class LoginForm(forms.Form):
    username = forms.CharField(label=u'Username')
    password = forms.CharField(max_length=30,
                               widget=forms.PasswordInput(render_value=False),
                               label=u'Password',)

    def clean(self):
        pass


class SignupForm(forms.Form):
    username = forms.CharField(required=True, label=u'Username')
    email = forms.EmailField(required=True, label=u'Email', help_text='A valid email address, please.')
    password = forms.CharField(required=True, max_length=30,
                               widget=forms.PasswordInput(render_value=False),
                               label=u'Password',)
    passwordc= forms.CharField(required=True, max_length=30,
                               widget=forms.PasswordInput(render_value=False),
                               label=u'Re Password',)
    
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).count()==1:
            raise forms.ValidationError("Username already in use!")
        return username
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).count()==1:
            raise forms.ValidationError("Email already in use!")
        return email


    def clean_passwordc(self):
        password=self.cleaned_data['password']
        passwordc=self.cleaned_data['passwordc']
        if password=='':
            raise forms.ValidationError("Please introduce a password!")
        if password!=passwordc:
            raise forms.ValidationError("Password doesn't match!")
        return passwordc
       

