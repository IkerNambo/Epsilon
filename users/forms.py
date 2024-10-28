from django import forms

from .models import SiteUsers




class UserForm(forms.Form):
    UserName = forms.CharField(label='UserName',widget=forms.TextInput(attrs=
                                                                       {'class': 'registerinput',
                                                                        'id': 'user-input'}))
    EmailAddress = forms.EmailField(label='EmailAddress',widget=forms.EmailInput(attrs=
                                                                        {'class': 'registerinput',
                                                                         'id': 'email-input',}))
    Password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'registerinput',
                                                                 'name': 'password-input'}), 
                               label='Password')
