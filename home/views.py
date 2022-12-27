from django.shortcuts import render


def index(request):
    """A view to return the index page"""
    return render(request, 'home/index.html')


def about_us(request):
    """A view to return the about us page"""
    return render(request, 'home/about_us.html')


def FAQ(request):
    """A view to return the FAQ us page"""
    return render(request, 'home/FAQ.html')
