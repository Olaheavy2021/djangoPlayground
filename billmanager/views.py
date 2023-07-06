from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings


# Create your views here.

def home(request):
    return render(request, 'billmanager/home.html', {'title': 'Welcome'})


def about(request):
    return render(request, 'billmanager/about.html', {'title': 'About'})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            email = EmailMessage(
                form.cleaned_data['subject'],
                form.cleaned_data['message'],
                form.cleaned_data['email'],
                [settings.EMAIL_HOST_USER]
            )

            email.send(fail_silently=False)

            messages.success(request, 'Your message has been sent. Thank you!')
            return render(request, 'billmanager/contact.html', {'title': 'Contact', 'form': ContactForm()})
        else:
            return render(request, 'billmanager/contact.html', {'title': 'Contact', 'form': form})
    else:
        form = ContactForm()
    return render(request, 'billmanager/contact.html', {'title': 'Contact', 'form': form})
