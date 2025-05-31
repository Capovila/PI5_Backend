from werkzeug.exceptions import HTTPException


class ResourceNotFoundException(HTTPException):
    code = 404
    description = "Resource not found"