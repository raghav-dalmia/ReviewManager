from django.shortcuts import render
from django.http import HttpResponse


def existInDb(username: str):
    return True

creatorDetail = {
    "name": "Mayank Chauhan",
    "about": "Using AI to create art which millions love! Reach out to cop the latest merch and t-shirt drops.",
    "socials": {
        "fb": "www.facebook.com",
        "ig": "www.facebook.com",
        "li": "www.facebook.com"
        },
    "profilePicture": "https://media.licdn.com/dms/image/D4E03AQFmhM-exDq7hA/profile-displayphoto-shrink_800_800/0/1670899588452?e=2147483647&v=beta&t=riu11uiHItprhol9CK2wvKbhCjOjRRWsk5rx2Pphzbw"
}

creatorReview = [
    {
        "author": "Mayank",
        "date": "29-3-2023",
        "content": "The watches sold are truly amazing. The watches sold are truly amazing. The watches sold are truly amazing."
    },
    {
        "author": "Raghav",
        "date": "01-3-2023",
        "content": "The tshirts sold are truly amazing. The watches sold are truly amazing. The watches sold are truly amazing."
    },
    {
        "author": "Aditya",
        "date": "10-3-2023",
        "content": "The hooodie sold are truly amazing. The watches sold are truly amazing. The watches sold are truly amazing."
    }
]

def myPage(request, username: str):
    context = {
        "creatorDetail": creatorDetail,
        "reviews": creatorReview
    }
    if not existInDb(username):
        return HttpResponse('Oops there is no creator by this name.')
    return render(request, 'creatorPage/index.html', context)