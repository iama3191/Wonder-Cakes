""" Imports from django and contact form. """
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


def contact(request):
    """
    View to display contact us form.

    If the form is valid, save, display a
    success message and return the contact us form.
    If invalid, display error message.
    """

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Thank you for your enquiry,\
                we will get back to soon!')

            return redirect('contact')
        else:
            messages.error(request,
                           'Something went wrong, please check the form')
    else:
        form = ContactForm()

    template = 'contact/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
