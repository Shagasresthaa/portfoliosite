from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import get_template, render_to_string
from django.conf import settings
from django.contrib import messages
from .forms import contactForm
import os
import requests


# Create your views here.

def contactPage(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        if form.is_valid():

            ''' reCAPTCHA validation '''
            recaptcha_response = request.POST.get('g-recaptcha-response')
            data = {
                'secret': settings.RECAPTCHA_PRIVATE_KEY,
                'response': recaptcha_response
                }
            r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
            result = r.json()

            print(result)

            if result['success']:
                name = form.cleaned_data['name']
                email = form.cleaned_data['email']
                message = form.cleaned_data['message']

                data = {"name":name, "email": email, "message": message}
                msg = render_to_string('contactform/emailtemplate.html', data)

                #print(msg)

                subject = "Contact from " + name
                
                sender = os.environ.get("EMAIL_HOST_USER")
                rsp = os.environ.get("EMAIL_RECIEPIENT")
    
                reciepient = []
                reciepient.append(rsp)
    
                # print(sender, reciepient)
    
                try:
                    send_mail(subject, message, sender, reciepient, html_message=msg) 
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                messages.success(request, "Your email has been sent" )
                return redirect ("contact")
                messages.error(request, "Error. Message not sent.")
    
                reciepient.clear()
    
                form = contactForm()
                return render(request, 'contactform/contactform.html', {'form': form, 'message': "Your Response has been successfully sent!"})
    
    form = contactForm()
    return render(request, 'contactform/contactform.html', {'form': form, 'recaptcha_site_key':settings.RECAPTCHA_PUBLIC_KEY})
