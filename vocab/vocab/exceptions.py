from rest_framework.exceptions import APIException

class InternalError(APIException):
    status_code = 500
    default_detail = 'Internal error'
