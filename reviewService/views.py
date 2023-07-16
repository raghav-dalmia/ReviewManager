from django.views import View
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from . import dao


class ReviewFormView(View):

    def get(self, request, username: str):
        context = {
            "username": username,
            "question": dao.get_review_question(request=request)
        }
        return render(request, './reviewForm.html', context=context)

    def post(self, request, username: str):
        ratings = int(request.POST.get('rating', 5))
        reviewee = str(request.POST.get('reviewee', '')).strip()
        feedback = str(request.POST.get('feedback', '')).strip()
        packaging = str(request.POST.get('packaging', '')).strip()
        attachments = request.FILES.getlist('attachment')
        dao.create_review(
            request=request,
            reviewee=reviewee,
            packaging=packaging,
            feedback=feedback,
            attachments=attachments,
            ratings=ratings,
        )
        messages.success(request, "Feedback submitted successfully.")
        return HttpResponse("Success")
