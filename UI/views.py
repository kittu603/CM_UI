from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserSqlDataForm , UserApiDataForm, UserSshDataForm




# Create your views here.

def index(request):
    return render(request,'UI/base.html')


def apiTab(request):
    return render(request,'UI/api.html', {'form': UserApiDataForm})

def sshTab(request):
    return render(request,'UI/ssh.html', {'form': UserSshDataForm})

def sqlTab(request):
    return render(request,'UI/sql.html', {'form': UserSqlDataForm})


