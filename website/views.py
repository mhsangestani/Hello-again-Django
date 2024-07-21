from django.shortcuts import render, HttpResponseRedirect
from website.forms import ContactForm, NewsletterForm
from .models import Contact
from django.contrib import messages

# Create your views here.

def index_view(request):
    return render(request, 'website/index.html')


def about_view(request):
    return render(request, 'website/about.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            messages.add_message(request, messages.SUCCESS, 'your ticket submited successfully')
            name = 'unknown'
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            Contact(name=name, email=email, subject=subject, message=message).save()
        else:
            messages.add_message(request, messages.ERROR, 'your ticket didnt submited')

    form = ContactForm()
    return render(request, 'website/contact.html', {'form':form})


def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'your Email submited successfully')
            return HttpResponseRedirect('/')
    else:
        
        return HttpResponseRedirect('/')

    form = NewsletterForm()
    return render(request, 'website/contact.html', {'form':form})
