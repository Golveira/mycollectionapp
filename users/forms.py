from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['username'].label = 'Usuário'
            self.fields['email'].label = 'Email'
            self.fields['password1'].label = 'Senha'
            self.fields['password2'].label = 'Confirmação senha'
            self.fields['username'].help_text = ''
            self.fields['password1'].help_text = ''
            self.fields['password2'].help_text = ''
            

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['username'].label = 'Usuário'
            self.fields['password'].label = 'Senha'


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['username'].label = 'Usuário'
            self.fields['first_name'].label = 'Nome'
            self.fields['last_name'].label = 'Sobrenome'
            self.fields['email'].label = 'Email'