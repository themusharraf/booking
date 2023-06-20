from collections import OrderedDict

from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response(OrderedDict([
            ('page', self.page.number),
            ('count', self.page.paginator.count),
            (self.page_size_query_param, self.page_size),
            ('results', data)
        ]))
