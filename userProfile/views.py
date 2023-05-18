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
            phonenumber = int(request.POST['phonenumber'])
            instagram = str(request.POST['instagram'])
            linkedin = str(request.POST['linkedin'])
            if not dao.models.utils.validPhoneNumber(phonenumber):
                messages.error(request, "Invalid phone number")
                return redirect('profile')
            dao.update_creator(user=request.user, email=email, firstname=firstname, lastname=lastname,
                               description=description, phonenumber=phonenumber, instagram=instagram, linkedin=linkedin)
            messages.success(request, "Profile update successfully")
        except:
            messages.error(request, "Something went wrong, please try again later.")
        return redirect('profile')
