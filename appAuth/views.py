from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from userProfile.dao import create_creator


def signup_user(request):
    if request.user.is_authenticated:
        return redirect('about')
    if request.method == "POST":
        username = str(request.POST['username'])
        password = str(request.POST['password'])
        try:
            creator = create_creator(username=username, password=password)
            user = authenticate(username=creator.user.username, password=password)
            if user is not None:
                login(request=request, user=user)
            messages.success(request, "Account created successfully.")
            return redirect('profile')
        except:
            messages.error(request, "Sorry, we are not able to create new account. Try to create account with different"
                           "username of login with " + username + " username.")
            return redirect('signup')

    else:
        return render(request, 'account/signup.html')


def login_user(request):
    if request.user.is_authenticated:
        return redirect('about')
    if request.method == "POST":
        username = str(request.POST['username'])
        password = str(request.POST['password'])

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request=request, user=user)
            messages.success(request, "Successfully signed as " + username)
            return redirect('about')
        else:
            messages.error(request, "Incorrect username or password.")
            return redirect('login')
    else:
        return render(request, 'account/login.html')


def logout_user(request):
    logout(request=request)
    return redirect('login')
