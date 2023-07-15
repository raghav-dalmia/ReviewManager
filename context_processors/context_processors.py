from ReviewManager import settings


def global_constants(request):
    return {
        'domain': 'https://127.0.0.1/' if settings.DEBUG else 'http://revulink.me/',
    }
