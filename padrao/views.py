from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

@login_required(login_url='/login/')
def index(request):
    return render(request, "padrao/home.html")


from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render, redirect

from django.contrib import messages


def login_user(request):
    return render(request,'login.html')


def registro(request):
    return render(request,'registro.html')



def logout_user(request):
    logout(request)
    return redirect('/')
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username,password=password)
        if usuario is not None:
            login(request,usuario)
            return redirect('/')
        else:
            messages.error(request,"Usuário ou senha invalido")


    return  redirect('/')









































