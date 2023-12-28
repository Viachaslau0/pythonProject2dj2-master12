from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.exceptions import ValidationError

class Login_inForm(forms.Form):
    email = forms.EmailField(label="Email",
                            widget=forms.TextInput(attrs={'class': 'form_input'}))
    password = forms.CharField(label="Password",
                               widget=forms.PasswordInput(attrs={'class': 'form_input'}))

class Sigh_inForm(UserCreationForm):
    email = forms.EmailField(label="Email",
                             widget=forms.TextInput(attrs={'class': 'form_input'}))
    password1 = forms.CharField(label="Password",
                                widget=forms.PasswordInput(attrs={'class': 'form_input'}))
    password2 = forms.CharField(label="Confirm Password",
                                widget=forms.PasswordInput(attrs={'class': 'form_input'}))

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if get_user_model().objects.filter(email=email).exists():
            raise ValidationError("Email already exists")
        return email