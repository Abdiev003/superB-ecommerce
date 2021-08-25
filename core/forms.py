from django import forms

from core.models import Subscribe, Contact


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'input-text',
            'id': 'billing:firstname',
            'title': 'First Name',
            'name': 'billing:firstname',
            'maxlength': 50,
        })
    )
    email = forms.CharField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'input-text',
            'id': 'billing:email',
            'title': 'Email Address',
            'name': 'billing:email',
            'maxlength': 254,
        })
    )
    company = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'input-text',
            'id': 'billing:company',
            'title': 'Company',
            'name': 'billing:company',
            'maxlength': 80,
        })
    )
    telephone = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'input-text',
            'id': 'billing:telephone',
            'title': 'Telephone',
            'name': 'billing:telephone',
            'maxlength': 13,
        })
    )
    address = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'input-text',
            'id': 'billing:address',
            'title': 'Street Address',
            'name': 'billing:address',
            'maxlength': 254,
        })
    )
    comment = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={
            'class': 'input-text',
            'id': 'comment',
            'title': 'Comment',
            'name': 'comment',
            'cols': '5',
            'rows': '3'
        })
    )

    class Meta:
        model = Contact
        fields = ('first_name', 'email', 'company',
                 'telephone', 'address', 'comment')


class SubscribeForm(forms.ModelForm):
    email = forms.CharField(
        strip=False,
        widget=forms.TextInput(attrs={
            'class': 'input-text required-entry validate-email',
            'value': 'Enter your email address',
            'onFocus': ' this.value="" ',
            'title': 'Sign up for our newsletter',
            'id': 'newsletter',
            'name': 'email',
        })
    )

    class Meta:
        model = Subscribe
        fields = ('email',)
