from django.shortcuts import redirect, render
from .models import contactus
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about_us(request):
    return render(request, 'about_us.html')

def login(request):
    return render(request, 'login.html')

def service(request):
    return render(request, 'service.html')

def modules(request):
    return render(request, 'modules.html')

def contact_us(request):
    return render(request, 'contact_us.html')

def contactus(request):
    if (request.method == 'POST'):
        firstname = request.POST.get('firstname')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        message = request.POST.get('message')
        resp = contactus(firstname=firstname, email=email, mobile=mobile, message=message)
        resp.save()
        messages.info(request, 'Message Received Successfully!!!')
        return redirect('contact_us.html')
    else:
        return render(request, 'contact_us.html')