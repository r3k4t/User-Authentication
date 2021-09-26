from django.shortcuts import render
from login_app.forms import UserForm,UserInfoForm
from login_app import forms

# Create your views here.

def index(request):
    dict = {}
    return render(request,'login_app/index.html',context=dict)

def register(request):
    user_form = UserForm()
    user_info_form = forms.UserInfoForm()
    dict = {'user_form':user_form, 'user_info_form':user_info_form}
    return render (request,'login_app/register.html',context=dict)