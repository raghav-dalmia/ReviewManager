import traceback
import logging
from datetime import datetime
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger("django")


class LogRequestExceptionMiddleware(MiddlewareMixin):
    EXCLUDE_PATHS = ["/favicon.ico/"]

    def process_exception(self, request, exception):
        if request.path in self.EXCLUDE_PATHS:
            return
        self.log_error("Path: " + request.path)
        self.log_error("Username: " + request.user.username)
        self.log_error("Email: " + request.user.email)
        self.log_error("Timestamp: " + str(datetime.now()))
        self.log_error(request.body)
        self.log_error(traceback.format_exc())
        return HttpResponse("in exception")
    
    @staticmethod
    def log_error(message: str):
        try:
            logger.error(message)
        except Exception as e:
            logger.error("Exception in log_error: " + str(e))
