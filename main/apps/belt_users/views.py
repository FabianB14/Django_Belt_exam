from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from django.contrib import messages 
from .models import *

def create_user(request):
    return render(request,'belt_users/registration.html')


def LogReg(request):
    response = ''
    response = LogUsers.objects.basic_registration(request.POST)
    
    if response['status']:
        request.session['user_id']= response['user_id']
        return redirect('wish_list/show_wish_list', messages)
    else:
        for error in response['errors']:
            messages.error(request,error)
        return redirect('/create_user')


def login(request):
    response = ''
    response = LogUsers.objects.basic_login(request.POST)
    print(response)
    
    if response['status']:
        request.session['user_id']= response['user_id']
        return redirect('wish_list/show_wish_list', messages)
    else:
        for error in response['errors']:
            messages.error(request,error)
            return redirect('/showLogin')
    return redirect('wish_list/show_wish_list')
    
def showLogin(request):
    return render(request,'belt_users/login.html')

# def profile(request):
#         if 'user_id' in request.session:
#             conext = {
#             'supa_user' : LogUsers.objects.get(id = request.session['user_id'])
#         }
        
#         return render(request,'belt_users/travels.html', conext)
def logOut(request):
    request.session.clear()
    return redirect('/showLogin')

def destination(request):
    print('hello')

    return render(request,'belt_users/destination.html')





# Create your views here.
