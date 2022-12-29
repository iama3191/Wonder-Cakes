from django import forms
from .models import Post


class AddPostForm(forms.ModelForm):
    """
    Add post form for admin only.
    """

    class Meta:
        """ Define form fields. """
        model = Post
        fields = ('title', 'slug', 'body', 'image')

    def clean_title(self):
        """ Capitalize post title. """
        return self.cleaned_data['title'].capitalize()

    def clean_body(self):
        """ Capitalize body text."""
        return self.cleaned_data['body'].capitalize()
