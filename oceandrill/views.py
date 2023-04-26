from django.shortcuts import render,redirect
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index.html',{})
def aboutUs(request):
    return render(request,'about-us.html',{})
def whatWeDo(request):
    return render(request,'what-we-do.html',{})
def ourWork(request):
    return render(request,'our-work.html',{})
def faq(request):
    return render(request,'faq.html',{})
def contactUs(request):
    form = ContactForm(request.POST or None)
    if request.method == 'POST': 
        form = ContactForm(request.POST or None)
        
        if form.is_valid():
            message = form.cleaned_data['message']
            first_name = form.cleaned_data['first_name']
            second_name = form.cleaned_data['second_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            subject = 'NEW CLIENT {} {} ({})'.format(first_name,second_name, email)
            body = message + "\n(Clients Phone Number) :" + " " + str(phone) + "\n (Clients Email) :" + " " + str(email)
            email = EmailMessage(subject, body, to=['odealtd@gmail.com'])
            email.send()
            print(form.cleaned_data)
            messages.success(request, 'Your form has been submitted successfully!')
            return redirect(contactUs)

        else:
            messages.error(request, 'Check your input and try again')
    else:
        form = ContactForm(request.POST or None)
    return render(request,'contact-us.html',{'form':form})
