from django.contrib.admin import ModelAdmin
from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(ModelAdmin):
    """
    Contact model view on django admin.
    """

    list_display = (
        'name',
        'email',
        'subject',
        'date',
    )
