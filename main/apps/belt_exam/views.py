from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
from django.contrib import messages 
from ..belt_users.models import LogUsers
from .models import wish_items

def show_wish_list(request):
    if 'user_id' not in request.session:
        return redirect('/showLogin')
    if 'user_id' in request.session:
            context = {
            'supa_user' : LogUsers.objects.get(id = request.session['user_id']),
            'wishes' :wish_items.objects.filter(wisher = request.session['user_id']),
            'other_wishers':wish_items.objects.exclude(wisher = request.session['user_id']),
            
        }
    return render(request,'belt_exam/wish_list.html',context)
def add_to_wish_list(request, wish_id):
    wish_items.objects.add_another_wish(request.session['user_id'], wish_id)
    return redirect('/wish_list/show_wish_list')
def remove_from_list(request, wish_id):
    wish_items.objects.remove_from_list(request.session['user_id'],wish_id)
    return redirect('/wish_list/show_wish_list')
def delete_item(request, wish_id):
    wish_items.objects.delete_item(request.session['user_id'], wish_id)
    return redirect('/wish_list/show_wish_list')

def show_add_wish(request):
    if 'user_id' not in request.session:
        return redirect('/showLogin')
    return render(request, 'belt_exam/add_wish.html')
def add_wish(request):
    response = wish_items.objects.add_wish(request.POST, request.session['user_id'])
    if response['status']:
        return redirect('/wish_list/show_wish_list', messages)
    else:
        for error in response['errors']:
            messages.error(request,error)
    return redirect('/wish_list/show_add_wish')
def wish_item(request, wish_id):
    if 'user_id' not in request.session:
        return redirect('/showLogin')
    context = {
        'wishes': wish_items.objects.get(id = wish_id)
    }
    return render(request,'belt_exam/wish_items.html',context)

# Create your views here.
