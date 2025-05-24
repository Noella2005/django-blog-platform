from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def account_home(request):
    return HttpResponse("This is the accounts home page.")
def register(request):
    return render(request, 'register.html')
