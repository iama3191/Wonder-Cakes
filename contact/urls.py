""" Imports from django and views. """
from django.urls import path
from . import views

# Url link to the contact page
urlpatterns = [
    path('', views.contact, name='contact')
]