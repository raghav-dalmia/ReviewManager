import traceback
import logging
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


logger = logging.getLogger("django")

class LogRequestExceptionMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        logger.error("Path: " + request.path)
        logger.error("Username: " + request.user.username)
        logger.error("Email: " + request.user.email)
        logger.error(request.body)
        logger.error(traceback.format_exc())
        return HttpResponse("in exception")
