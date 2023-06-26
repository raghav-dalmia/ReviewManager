from django.views import View
from django.contrib import messages
from django.shortcuts import render, redirect
from . import dao


class ProfileView(View):

    def get(self, request):
        creator = dao.get_creator_from_username(request.user)
        context = {
            "creator": creator
        }
        return render(request, 'components/profile.html', context=context)

    def post(self, request):
        profile_picture = request.FILES.get('profile')
        email = str(request.POST['email'])
        firstname = str(request.POST['firstname'])
        lastname = str(request.POST['lastname'])
        description = str(request.POST['description'])
        question = str(request.POST['question'])
        numberOfResults = int(request.POST['numberOfResults'])
        orderBy = int(request.POST['orderBy'])
        instagram = str(request.POST['instagram'])
        linkedin = str(request.POST['linkedin'])
        facebook = str(request.POST['facebook'])
        website = str(request.POST['website'])
        twitter = str(request.POST['twitter'])
        youtube = str(request.POST['youtube'])
        dao.update_creator(user=request.user,
                           email=email,
                           firstname=firstname,
                           lastname=lastname,
                           description=description,
                           instagram=instagram,
                           linkedin=linkedin,
                           question=question,
                           numberOfResults=numberOfResults,
                           facebook=facebook,
                           orderBy=orderBy,
                           profile_picture=profile_picture,
                           website=website,
                           twitter=twitter,
                           youtube=youtube)
        messages.success(request, "Profile update successfully")
        return redirect('profile')