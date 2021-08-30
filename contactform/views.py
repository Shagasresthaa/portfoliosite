from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.core.mail import send_mail
from .forms import contactForm
import os

# Create your views here.

def contactPage(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            subject = "Contact from " + name + " with email " + email
            
            sender = os.environ.get("EMAIL_HOST_USER")
            rsp = os.environ.get("EMAIL_RECIEPIENT")

            reciepient = []
            reciepient.append(rsp)

            # print(sender, reciepient)

            send_mail(subject, message, sender, reciepient)

            reciepient.clear()

            form = contactForm()
            return render(request, 'contactform/contactform.html', {'form': form, 'message': "Your Response has been successfully sent!"})
    
    form = contactForm()
    return render(request, 'contactform/contactform.html', {'form': form})
