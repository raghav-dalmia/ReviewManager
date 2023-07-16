from ReviewManager import settings


def global_constants(request):
    return {
        'domain': "https://%s/" % (settings.ALLOWED_HOSTS[0]),
        'media_url': settings.MEDIA_URL
    }
