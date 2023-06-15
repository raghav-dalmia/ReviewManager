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
        return render(request, 'components/profile.html', context=context)

    def post(self, request):
        email = str(request.POST['email'])
        firstname = str(request.POST['firstname'])
        lastname = str(request.POST['lastname'])
        description = str(request.POST['description'])
        question = str(request.POST['question'])
        numberOfResults = int(request.POST['numberOfResults'])
        orderBy = int(request.POST['orderBy'])
        phonenumber = int(request.POST['phonenumber'])
        instagram = str(request.POST['instagram'])
        linkedin = str(request.POST['linkedin'])
        if not dao.models.utils.validPhoneNumber(phonenumber):
            messages.error(request, "Invalid phone number")
            return redirect('profile')
        dao.update_creator(user=request.user,
                           email=email,
                           firstname=firstname,
                           lastname=lastname,
                           description=description,
                           phonenumber=phonenumber,
                           instagram=instagram,
                           linkedin=linkedin,
                           question=question,
                           numberOfResults=numberOfResults,
                           orderBy=orderBy)
        messages.success(request, "Profile update successfully")
        return redirect('profile')
