from rest_framework.views import exception_handler
from django.http import Http404


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if isinstance(exc, Http404):
        response.data = {'error': 'topilmadi'}
    return response
