from django.views import View
from django.shortcuts import redirect, render
from django.contrib import messages
from . import dao


class ReviewFormView(View):

    def get(self, request, username: str):
        context = {
            "username": username,
            "question": dao.get_review_question(username=username)
        }
        return render(request, './reviewForm.html', context=context)

    def post(self, request, username: str):
        ratings = int(request.POST['rating'])
        reviewee = str(request.POST['reviewee'])
        feedback = str(request.POST['feedback'])
        packaging = str(request.POST['packaging'])
        attachments = request.FILES.getlist('attachment')
        dao.create_review(
            username=username,
            reviewee=reviewee,
            packaging=packaging,
            feedback=feedback,
            attachments=attachments,
            ratings=ratings,
        )
        messages.success(request, "Feedback submitted successfully.")
        return redirect('reviewForm', username=username)
