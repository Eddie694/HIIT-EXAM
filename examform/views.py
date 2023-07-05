from django.shortcuts import render
from .models import ContactUs
from django.contrib import messages


# Create your views here.

def home(request):

    #getting the input from the template and sendingt to the backend
    if request.method == 'POST':
        name =request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        messageus = request.POST.get('messageus')

        customer = ContactUs.objects.create(name=name, email=email,subject=subject,messageus=messageus)
        customer.save()
        # to return a message to the customer
        messages.success(request, "Your message has been successfully sent") 

        
    return render(request, 'examform/form.html', {})
