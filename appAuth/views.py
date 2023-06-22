from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.decorators.cache import never_cache
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from userProfile.dao import create_creator


@never_cache
def signup_user(request):
    if request.user.is_authenticated:
        return redirect('creatorAnalytics', num_days=7)
    if request.method == "POST":
        username = str(request.POST['username'])
        password = str(request.POST['password'])
        try:
            creator = create_creator(username=username, password=password)
            user = authenticate(username=creator.user.username, password=password)
            if user is not None:
                login(request=request, user=user)
            messages.success(request, "Account created successfully.")
            return redirect('creatorAnalytics', num_days=7)
        except:
            messages.error(request, "Sorry, we are not able to create new account. Try to create account with different"
                           "username of login with " + username + " username.")
            return redirect(reverse('signup'))

    else:
        return render(request, 'account/signup.html')


@never_cache
def login_user(request):
    if request.user.is_authenticated:
        return redirect('creatorAnalytics', num_days=7)
    if request.method == "POST":
        username = str(request.POST['username'])
        password = str(request.POST['password'])

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request=request, user=user)
            messages.success(request, "Successfully signed as " + username)
            return redirect('creatorAnalytics', num_days=7)
        else:
            messages.error(request, "Incorrect username or password.")
            return redirect(reverse('login'))
    else:
        return render(request, 'account/login.html')


@never_cache
def logout_user(request):
    logout(request=request)
    return redirect(reverse('login'))
