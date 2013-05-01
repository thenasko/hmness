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


