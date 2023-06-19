from datetime import date
from creatorPage.models import PageView


class PageViewMiddleware:
    EXCLUDED_PATHS = ['/static', '/media', '/admin', '/favicon.ico']

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not self.should_exclude(request):
            response = self.get_response(request)
            self.save_page_view(request)
            return response

        return self.get_response(request)

    def should_exclude(self, request):
        path = request.path_info
        if request.user.is_superuser:
            return True
        for excluded_path in self.EXCLUDED_PATHS:
            if path.startswith(excluded_path):
                return True
        return False

    @staticmethod
    def save_page_view(request):
        url = request.build_absolute_uri()
        request_type = request.method
        page_visit, created = PageView.objects.get_or_create(date=date.today(), url=url, request_type=request_type)
        page_visit.visit_count += 1
        page_visit.save()