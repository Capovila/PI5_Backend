from flask import jsonify
from werkzeug.exceptions import HTTPException

from src.domain.exceptions.BadRequestException import BadRequestException
from src.domain.exceptions.ResourceNotFoundException import ResourceNotFoundException


class ExceptionHandler:
    def __init__(self,app):
        self.app = app
        self._register_handlers()

    def _register_handlers(self):
        self.app.register_error_handler(HTTPException, self.handleResourceNotFound)
        self.app.register_error_handler(BadRequestException, self.handleBadRequest)
        self.app.register_error_handler(Exception, self.handleGenericException)

    def handleResourceNotFound(self, exception: ResourceNotFoundException):
        response = jsonify(
            {
                "message": exception.description,
            }
        ), exception.code
        return response

    def handleBadRequest(self, exception: BadRequestException):
        response = jsonify(
            {
                "message": exception.description,
            }
        ), exception.code
        return response

    def handleGenericException(self, exception):

        response = jsonify({
            "message": "Erro interno do servidor"
        })
        return response, 500