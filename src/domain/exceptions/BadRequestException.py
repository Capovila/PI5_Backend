from werkzeug.exceptions import HTTPException


class BadRequestException(HTTPException):
    code = 400
    description = "Bad Request"