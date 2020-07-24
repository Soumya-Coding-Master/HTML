from django.shortcuts import render
from django.http import HttpResponse
import datetime
def home(request):
    return render(request, 'index1.html')
def add(request):
    f=request.POST['firstname']
    l=request.POST['lastname']
    hello=(f"{f} {l}")
    return render(request, 'results.html',{'name':hello})


def exam(request):
    return render(request, 'hola.html')  


def password(request):
    import password
    u=password.Password()
    x=u.generating_password()
    return render(request, 'start.html',{'password':x})


def user_info(request):
    return render(request, 'user.html')

