from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler

from apps.cars.choices.body_type_choices import BodyTypeChoices


def error_handler(ext: Exception, context: dict) -> Response:
    handlers = {
        'JwtException': _jwt_validation_error_handler,
        'BodyTypeException': _body_type_error_handler,
    }

    response = exception_handler(ext, context)
    exc_class = ext.__class__.__name__

    if exc_class in handlers:
        return handlers[exc_class](ext, context)

    return response


def _jwt_validation_error_handler(ext: Exception, context: dict) -> Response:
    return Response({'detail': 'Token is invalid or expired'}, status=status.HTTP_403_FORBIDDEN)


def _body_type_error_handler(ext: Exception, context: dict) -> Response:
    valid_choices = [choice[1] for choice in BodyTypeChoices.choices]
    return Response({'detail': 'Not available choose: ' + ', '.join(valid_choices)},
                    status=status.HTTP_400_BAD_REQUEST)
