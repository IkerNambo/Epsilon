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
   
    username = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                                'class': 'form-control',
                                                                }))
    email = forms.CharField(label='',widget=forms.EmailInput(attrs={'placeholder': 'Email',
                                                                'class': 'form-control',
                                                                }))
    password1 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                'class': 'form-control',
                                                                'label': 'password'
                                                                }))
    password2 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
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
    css_error_class = 'error-text'
    
    
    
    class Meta:
        model = User
        fields = ['email']
        
        
        
    email = forms.CharField(label='', widget=forms.EmailInput(attrs={'placeholder': 'New Email',
                                                                'class': 'form-control-global',
                                                                }))
    def clean_email(self):
        email = self.cleaned_data['email']
        
        if User.objects.filter(email=email).exists():
            raise ValidationError('Email is already in use')
        return email
    
class ChangePasswordForm(PasswordChangeForm):
    
    old_password = forms.CharField(label='',required=True, widget=forms.PasswordInput(attrs={
        'placeholder': 'old password',
        'class': 'form-control-global password-control',
    }))
    new_password1 = forms.CharField(label='',required=True, widget=forms.PasswordInput(attrs={
        'placeholder': 'New password',
        'class': 'form-control-global password-control',
    }))
    new_password2 = forms.CharField(label='',required=True, widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm New password',
        'class': 'form-control-global password-control',
    }))


class ChangeUsernameForm(UserChangeForm):
    email = None
    password = None
    css_error_class = 'error-text'
    
    class Meta:
        model = User
        fields = ['username']
        help_texts = {
            'username': None,
        }
        
    username = forms.CharField(label='',max_length=20,widget=forms.TextInput(attrs={'placeholder': 'New username',
                                                                'class': 'form-control-global',
                                                                }))
        
    def clean_username(self):
        username = self.cleaned_data['username']
            
        if User.objects.filter(username=username).exists():
            raise ValidationError('Username is already in use')
        return username
        
 
            
