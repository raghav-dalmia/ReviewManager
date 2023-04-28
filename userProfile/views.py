from django.views import View
from django.contrib import messages
from django.shortcuts import render, redirect
from . import dao


class ProfileView(View):

    def get(self, request):
        creator = dao.get_creator(request.user)
        context = {
            "creator": creator
        }
        return render(request, 'profile.html', context=context)

    def post(self, request):
        try:
            email = str(request.POST['email'])
            firstname = str(request.POST['firstname'])
            lastname = str(request.POST['lastname'])
            description = str(request.POST['description'])
            creator = dao.get_creator(request.user)
            creator.description = description
            creator.user.email = email
            creator.user.first_name = firstname
            creator.user.last_name = lastname
            creator.user.save()
            creator.save()
            messages.success(request, "Profile update successfully")
        except:
            messages.error(request, "Something went wrong, please try again later.")
        return redirect('profile')
