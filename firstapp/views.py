from django.shortcuts import render , HttpResponse
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    return HttpResponse('Welcome to your page')


def users(request):
    users = User.objects.all()
    return render(request , 'userList.html' , {'users' :users})
