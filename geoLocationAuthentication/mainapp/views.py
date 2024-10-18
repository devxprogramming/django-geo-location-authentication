from django.shortcuts import render, redirect, resolve_url
from django.http import HttpResponse
from .models import User, UserSession
from .forms import UserForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
import geocoder
from .utils import get_client_ip

@login_required(login_url='login')
def home(request):
    return render(request, 'mainapp/home.html')


def signup(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            client_ip = get_client_ip()
            new_user.ip_address = client_ip['ip_address']
            new_user.longitude = client_ip['longitude']
            new_user.latitude = client_ip['latitude']
            new_user.save()
            return redirect('login')
    context = {'form': form}
    return render(request, 'mainapp/signup.html', context)


def login_user(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if UserSession.objects.filter(user=user).exists():
                request.session['user'] = user.username
                return redirect('terminate')
            login(request, user)
            # Store the username in the session 
            return redirect('home')
    context = {'form': form}
    return render(request, 'mainapp/login.html', context)


def logout_user(request):
    user = request.user
    UserSession.objects.filter(user=user).delete()
    logout(request)
    return redirect('login')


def terminate(request):
    user = request.session.get('user')
    context = {'user': user}
    return render(request, 'mainapp/terminate.html', context)