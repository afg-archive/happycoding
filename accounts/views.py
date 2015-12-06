from django import forms
from django.contrib import messages
from django.contrib.auth import login as login_user, logout as logout_user
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404 as go404
from problem.models import Code, Hint, Upvote, HintUpvote
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
                return redirect(request.GET.get('next') or '/')
    else:
        form = AuthForm()
    return render(request, 'login.html', {'form': form})


def logout(request):
    logout_user(request)
    return redirect(request.GET.get('next') or '/')


def profile(request, pk):
    # XXX
    # PLEASE AWARE PERFORMANCE ISSUES HERE
    user = go404(User, pk=pk)
    user_code = Code.objects.filter(user=user)
    user_hint = Hint.objects.filter(user=user)
    shares = user_code.count()
    share_upvotes = Upvote.objects.filter(code__in=user_code).count()
    hints = user_hint.count()
    hint_upvotes = HintUpvote.objects.filter(hint__in=user_hint).count()
    return render(
        request,
        'profile.html',
        {
            'user': user,
            'shares': shares,
            'share_upvotes': share_upvotes,
            'hints': hints,
            'hint_upvotes': hint_upvotes,
            'sum': shares+share_upvotes+hints+hint_upvotes
        }
    )
