from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model, password_validation
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class RegisterForm(UserCreationForm):
    email = forms.CharField(
        label=_("Email"),
        strip=False,
        widget=forms.TextInput(attrs={
            'class': 'input-text',
            'id': 'email',
            'name': 'email',
            'title': 'Email'
        })
    )
    first_name = forms.CharField(
        label=_("First Name"),
        strip=False,
        widget=forms.TextInput(attrs={
            'class': 'input-text',
            'id': 'fName',
            'name': 'fName',
            'title': 'First Name',
            'maxlength': 50,
        })
    )
    last_name = forms.CharField(
        label=_("Last Name"),
        strip=False,
        widget=forms.TextInput(attrs={
            'class': 'input-text',
            'id': 'lName',
            'name': 'lName',
            'title': 'Last Name',
            'maxlength': 50,
        })
    )
    image = forms.FileField(
        widget=forms.FileInput(attrs={
            'class': 'input-text',
            'accept': '.jpg, .png',
            'id': 'image',
            'name': 'image',
            'title': 'Profile Image'
        })
    )
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'class': 'input-text',
            'id': 'pass',
            'name': 'pass',
            'title': 'Password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password Confirm"),
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'class': 'input-text',
            'id': 'pass2',
            'name': 'pass2',
            'title': 'Confirm Password'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name',
                  'password1', 'password2', 'image')


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label=_("Email"),
        widget=forms.EmailInput(attrs={
            'class': 'input-text',
            'id': 'email',
            'name': 'email',
            'title': 'Email',
        })
    )
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={
            'autocomplete': 'new-password',
            'class': 'input-text',
            'id': 'pass',
            'name': 'pass',
            'title': 'Password',
        }),
    )


class UpdateProfile(forms.ModelForm):
    first_name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            "id": "firstname",
            "class": "input-text required-entry",
            "title": "First Name",
            "maxlength": 50,
        })
    )
    last_name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            "id": "lastname",
            "class": "input-text required-entry",
            "title": "Last Name",
            "maxlength": 50,
        })
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name')
