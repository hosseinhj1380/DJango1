from django.views import View
from accounts.models import User
# from django.http import HttpResponse
from django.shortcuts import render
def about_us(request):
    # if request=='GET':
        user=User.objects.all()
        return render (request,'about_us.html',context={'users':user})