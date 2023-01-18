from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib import messages

def signin(request):
    if request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, 'Please logout to make that action.')
        return HttpResponseRedirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if request.GET.get('next'):
                    return HttpResponseRedirect(request.GET.get('next'))
                messages.add_message(request, messages.SUCCESS, 'Successfully logged in.')
                return HttpResponseRedirect('/')
            else:
                messages.add_message(request, messages.ERROR, 'Oops! Incorrect details.')
                return HttpResponseRedirect('signin')

        return render(request, 'accounts/signin.html')

def signup(request):
    if request.user.is_authenticated:
        messages.add_message(request, messages.ERROR, 'Please logout to create another account.')
        return HttpResponseRedirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password1 = request.POST.get('password1')

            if not username:
                messages.add_message(request, messages.ERROR, 'Username cannot be empty.')
                return HttpResponseRedirect('signup')
            if not email:
                messages.add_message(request, messages.ERROR, 'Email cannot be empty.')
                return HttpResponseRedirect('signup')
            if not password:
                messages.add_message(request, messages.ERROR, 'Password cannot be empty.')
                return HttpResponseRedirect('signup')
            if not password1:
                messages.add_message(request, messages.ERROR, 'Confirmation password cannot be empty.')
                return HttpResponseRedirect('signup')

            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                if password == password1:
                    user = User.objects.create_user(username, email, password)
                    messages.add_message(request, messages.SUCCESS, 'Account created successfully. Login.')
                    return HttpResponseRedirect('signin')
                else:
                    messages.add_message(request, messages.ERROR, 'Oops! Your passwords do not match.')
                    return HttpResponseRedirect('signup')
            else:
                messages.add_message(request, messages.ERROR, 'Username already exist.')
                return HttpResponseRedirect('signup')

        return render(request, 'accounts/signup.html')

def signout(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, 'Thank you for visiting our site today.')
    return HttpResponseRedirect('/')
