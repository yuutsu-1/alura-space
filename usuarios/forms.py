from django import forms
from django.contrib.auth.models import User

class LoginForms(forms.Form):
    next = forms.CharField(widget=forms.HiddenInput(), required=False)
    username = forms.CharField(
        label = "Usuário",
        required = True,
        max_length = 50,
        widget = forms.TextInput(attrs={
            'class': 'login__input',
            'placeholder': 'Digite seu usuário'
            })
    )
    password = forms.CharField(
        label = "Senha",
        required = True,
        min_length = 8,
        max_length = 50,
        widget = forms.PasswordInput(attrs={
            'class': 'login__input',
            'placeholder': 'Digite sua senha'
            })
    )
    
class SignupForms(forms.Form):
    next = forms.CharField(widget=forms.HiddenInput(), required=False)
    username = forms.CharField(
        label = 'Usuário',
        required = True,
        max_length = 50,
        widget = forms.TextInput(attrs={
            'class': 'login__input',
            'placeholder': 'Escolha seu usuário'
            })
    )
    email = forms.EmailField(
        label = 'Email',
        required = True,
        max_length = 50,
        widget = forms.EmailInput(attrs={
            'class': 'login__input',
            'placeholder': 'Digite seu email'
            })
    )
    password = forms.CharField(
        label = 'Senha',
        required = True,
        min_length = 8,
        max_length = 50,
        widget = forms.PasswordInput(attrs={
            'class': 'login__input',
            'placeholder': 'Crie sua senha'
            })
    )
    password2 = forms.CharField(
        label = 'Confirmar Senha',
        required = True,
        min_length = 8,
        max_length = 50,
        widget = forms.PasswordInput(attrs={
            'class': 'login__input',
            'placeholder': 'Confirme sua senha'
            })
    )
    
    def clean(self):
        cleaned_data = super().clean()

        
        if cleaned_data['password'] != cleaned_data['password2']:
            raise forms.ValidationError({'password2': 'As senhas não conferem'}, code='usr01')
        
        if User.objects.filter(username=cleaned_data['username']).exists():
            raise forms.ValidationError({'username': 'Usuário já existe'}, code='usr02')
        
        return cleaned_data
