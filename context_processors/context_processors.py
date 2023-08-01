from ReviewManager import settings
LOCAL_HOST = '127.0.0.1:8000'


def global_constants(request):
    return {
        'domain':  "https://%s" % settings.DOMAIN_NAME if settings.PROD_SERVER else LOCAL_HOST,
        'media_url': settings.MEDIA_URL
    }
