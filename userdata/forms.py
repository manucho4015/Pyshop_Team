from django import forms
from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

User = get_user_model()


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name...'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name...'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username...'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email Address...'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password...'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password...'}))

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]
        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'input'}),
        #     'email': forms.EmailInput(attrs={'class': 'input'}),
        #     'password1': forms.PasswordInput(attrs={'class': 'input'}),
        #     'password2': forms.PasswordInput(attrs={'class': 'input'}),
        # }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_qs = User.objects.filter(email=email)
        if email_qs.exist():
            raise forms.ValidationError('This email is already being used')
        return email


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username...'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password...'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('This user does not exist')
            if not user.check_password(password):
                raise forms.ValidationError('Incorrect password')
            if not user.is_active:
                raise forms.ValidationError('This user is not active')
        return super(LoginForm, self).clean(*args, **kwargs)

    class Meta:

        fields = ["username", "password"]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input'}),
            'password': forms.PasswordInput(attrs={'class': 'input'}),
        }
