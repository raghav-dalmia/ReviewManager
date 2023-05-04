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
        return render(request, 'review_form.html', context=context)

    def post(self, request, username: str):
        rating = int(request.POST['rating'])
        feedback = str(request.POST['feedback'])
        attachment = request.FILES.getlist('attachment')
        dao.create_review(
            username=username,
            ratings=rating,
            feedback=feedback,
            attachments=attachment
        )
        messages.success(request, "Feedback submitted successfully.")
        return redirect('reviewForm', username=username)
