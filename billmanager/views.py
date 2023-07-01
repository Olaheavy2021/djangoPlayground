from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'billmanager/home.html', {'title': 'Welcome'})


def about(request):
    return render(request, 'billmanager/about.html', {'title': 'About'})


def contact(request):
    return render(request, 'billmanager/contact.html', {'title': 'Contact'})
