from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

from .forms import SignUpForm


# Redirect user based on role
def redirect_user(user):
    if user.is_superuser or user.is_staff:
        return redirect('admin_dashboard')

    return redirect('home')


# Login view
def login_view(request):
    if request.user.is_authenticated:
        return redirect_user(request.user)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            messages.success(request, f'Welcome back, {user.username}!')

            return redirect_user(user)

        else:
            messages.error(request, 'Invalid username or password.')

    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})


# Signup view
def signup(request):
    if request.user.is_authenticated:
        return redirect_user(request.user)

    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            messages.success(request, f'Welcome to QuickMart, {user.username}!')

            return redirect('home')

    else:
        form = SignUpForm()

    return render(request, 'registration/signup.html', {'form': form})