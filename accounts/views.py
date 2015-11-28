from django import forms
from django.contrib import messages
from django.contrib.auth import login as login_user, logout as logout_user
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
import oj


class AuthForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


def login(request):
    if request.method == 'POST':
        form = AuthForm(request.POST)
        if form.is_valid():
            try:
                oj.login_session(**form.cleaned_data)
            except oj.LoginFailed:
                messages.error(request, 'Login Failed. Incorrect username or password.')
            else:
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                request.session['password'] = password
                try:
                    user = User.objects.get(username=username)
                except User.DoesNotExist:
                    user = User.objects.create_user(username=username)
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                login_user(request, user)
                return redirect('/')
    else:
        form = AuthForm()
    return render(request, 'login.html', {'form': form})


def logout(request):
    logout_user(request)
    return redirect('/')
