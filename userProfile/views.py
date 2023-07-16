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
        print("update profile")
        profile_picture = request.FILES.get('profile')
        print(profile_picture)
        email = str(request.POST.get('email', '')).strip()
        firstname = str(request.POST.get('firstname', '')).strip()
        lastname = str(request.POST.get('lastname', '')).strip()
        description = str(request.POST.get('description', '')).strip()
        question = str(request.POST.get('question', '')).strip()
        numberOfResults = int(request.POST.get('numberOfResults', ''))
        orderBy = int(request.POST.get('orderBy', ''))
        instagram = str(request.POST.get('instagram', '')).strip()
        linkedin = str(request.POST.get('linkedin', '')).strip()
        facebook = str(request.POST.get('facebook', '')).strip()
        website = str(request.POST.get('website', '')).strip()
        twitter = str(request.POST.get('twitter', '')).strip()
        youtube = str(request.POST.get('youtube', '')).strip()
        dao.update_creator(request=request,
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