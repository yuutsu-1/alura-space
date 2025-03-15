from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from usuarios.forms import LoginForms, SignupForms
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def login(request: HttpRequest):
    form = LoginForms()
    
    if request.method == 'POST':
        form = LoginForms(request.POST)
        
        if not form.is_valid():
            return render(request, 'usuarios/partials/_login.html', {'form': form})
        
        usuario = authenticate(
            request = request,
            username = form['username'].value(),
            password = form['password'].value()
        )
        
        if usuario:
            auth_login(request, usuario)
            return HttpResponse()
        
        form.add_error('password', 'Usuário ou senha inválidos')
        
    return render(request, 'usuarios/partials/_login.html', {'form': form})


def signup(request: HttpRequest):
    if request.method == 'POST':
        form = SignupForms(request.POST)
        
        if not form.is_valid():
            return render(request, 'usuarios/partials/_signup.html', {'form': form})
        
        user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password'],
            email=form.cleaned_data['email']
        )
        
        user.save()
                
        return redirect('/auth?type=login')

@login_required
def logout(request: HttpRequest):
    auth_logout(request)
    return redirect('/')

def auth(request: HttpRequest):
    auth_type = request.GET.get('type', 'login')
    
    if auth_type == 'login':
        next_url = request.GET.get('next', request.path)
        
        form = LoginForms(initial={'next': next_url})
        template = 'usuarios/partials/_login.html'
        
    elif auth_type == 'signup':
        next_url = request.GET.get('next', request.path)
        form = SignupForms(initial={'next': next_url})
        template = 'usuarios/partials/_signup.html'
        
    return render(request, template, {'form': form})


