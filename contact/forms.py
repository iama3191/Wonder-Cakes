""" Imports from django and contact model. """
from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Contact form to make enquiries.
    """

    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Name'}),
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email'}),
    )

    query = forms.CharField(
        widget=forms.Textarea(
            attrs={'placeholder': 'Please enter your query details'}),
    )

    class Meta:
        """ Define booking form fields and widgets. """

        model = Contact
        fields = "__all__"
        widgets = {
            'subject': forms.RadioSelect()
        }