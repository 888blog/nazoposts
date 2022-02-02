from django import forms
from django.core.exceptions import ValidationError

from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    username = forms.CharField(required=True,
                                max_length=30,
                                widget=forms.TextInput(
                                    attrs={
                                        'placeholder': 'ユーザー名'
                                    }
                                ),)
    
    password = forms.CharField(required=True,
                                max_length=255,
                                widget=forms.PasswordInput(
                                    attrs={
                                        'placeholder': 'パスワード'
                                    }
                                ))


    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        if 'username' and 'password' in cleaned_data:
            auth_result = authenticate(username=cleaned_data['username'], password=cleaned_data['password'])
            if not auth_result:
                raise ValidationError('ユーザー名またはパスワードが違います')
        return cleaned_data

    def clean_username(self):
        username = self.cleaned_data['username']
        return username

    def clean_password(self):
        password = self.cleaned_data['password']
        return password