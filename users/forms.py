from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, UserChangeForm
from django.contrib.auth import get_user_model 
from django.core.exceptions import ValidationError


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
    def clean_email(self):
        email = self.cleaned_data['email']
        
        if User.objects.filter(email=email).exists():
            raise ValidationError('Email already exists')
        return email
    
class ChangePasswordForm(PasswordChangeForm):
    pass

class ChangeEmailForm(UserChangeForm):
    password = None
    username = None
    error_class = 'error-control'
    
    
    class Meta:
        model = User
        fields = ['email']
        
        
    email = forms.CharField(label='Enter new email', widget=forms.EmailInput(attrs={'placeholder': 'Email',
                                                                'class': 'form-control-global',
                                                                }))
    def clean_email(self):
        email = self.cleaned_data['email']
        
        if User.objects.filter(email=email).exists():
            raise ValidationError('Email is already in use ')
        return email
    
class ChangePasswordForm(PasswordChangeForm):
    
    old_password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'placeholder': 'old password',
        'class': 'form-control-global password-control',
    }))
    new_password1 = forms.CharField(label='New Password',required=True, widget=forms.PasswordInput(attrs={
        'placeholder': 'New password',
        'class': 'form-control-global password-control',
    }))
    new_password2 = forms.CharField(label='Confirm New Password',required=True, widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm New password',
        'class': 'form-control-global password-control',
    }))
    
    
    
