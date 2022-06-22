from django.test import TestCase


from django.core.mail import send_mail
from .forms import contactForm
import os

# Create your tests here.
class contactFormTestCases(TestCase):
    def testvalidForm(self):
        formData = {"name":"test","email":"foo@testing.com","message":"This is a test message"}
        f = contactForm(data=formData)
        self.assertTrue(f.is_valid())
    
    def testInvalidEmailForm(self):
        formData = {"name":"test","email":"foo@.com","message":"This is a test message"}
        f = contactForm(data=formData)
        self.assertFalse(f.is_valid())

    def testEmptyNameForm(self):
        formData = {"name":"","email":"foo@testing.com","message":"This is a test message"}
        f = contactForm(data=formData)
        self.assertFalse(f.is_valid())

    def testEmptyEmailForm(self):
        formData = {"name":"test","email":"","message":"This is a test message"}
        f = contactForm(data=formData)
        self.assertFalse(f.is_valid())

    def testEmptyMessageForm(self):
        formData = {"name":"test","email":"foo@testing.com","message":""}
        f = contactForm(data=formData)
        self.assertFalse(f.is_valid())

    def testEmailBackend(self):
        name = "Test User"
        email = "foo@testing.com"
        message = "This is testing email"            
        subject = "Contact from " + name + " with email " + email            
        sender = os.environ.get("EMAIL_HOST_USER")
        rsp = os.environ.get("EMAIL_RECIEPIENT")
        reciepient = []
        reciepient.append(rsp)
        resp = send_mail(subject, message, sender, reciepient)
        self.assertEqual(resp, 1)