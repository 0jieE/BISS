from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate,login
from django.http import JsonResponse
from .models import User
from .forms import  LoginForm


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_superuser:
                login(request, user)
                return redirect('/admin')
            elif user is not None and user.is_staff:
                login(request, user)
                return redirect('/profile-list')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'accounts/login.html', {'form': form, 'msg': msg})

def logout_view(request):
  logout(request)
  return redirect('login')