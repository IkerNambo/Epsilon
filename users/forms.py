from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import get_user_model 

CustomUserUserUser = get_user_model()


class UserForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
    class Meta: 
        model = User
        fields = ['username',
                  'email', 
                  'password1']
        help_texts = {
            'username': None,
            'email': None,
        }
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                                'class': 'form-control',
                                                                }))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder': 'Email',
                                                                'class': 'form-control',
                                                                }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                'class': 'form-control',
                                                                'label': 'password'
                                                                }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                'class': 'form-control',
                                                                'label': 'password'
                                                                }))
    
class ChangePasswordForm(PasswordChangeForm):
    pass


