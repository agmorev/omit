from django import forms
from django.core.mail import EmailMessage
from django.utils.translation import gettext_lazy as _


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=200)
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)
    
    def send_email(self):
        # send email using the self.cleaned_data dictionary
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        subject = self.cleaned_data['subject']
        message = f"Message from {name} <br> Email: {email} <br> Subject: {subject} <br> Message: { self.cleaned_data['message'] }"
        msg = EmailMessage(
                subject,
                message,
                email,
                ['contact@omorev.pp.ua', ],
            )
        msg.content_subtype = "html"
        msg.send()