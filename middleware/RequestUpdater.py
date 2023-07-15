from userProfile import dao as userDao

class RequestUpdater:
    def __init__(self, get_response):
        self.get_response = get_response

    def process_request(self, request):
        if request.user.is_authenticated:
            request.creator = userDao.get_creator(request.user)
        return None

    def __call__(self, request):
        response = self.process_request(request)
        if response is None:
            response = self.get_response(request)
        return response
