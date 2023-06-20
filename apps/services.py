from copy import copy
from datetime import datetime

from django.utils.timezone import now

from apps.models import Book
from apps.serializers import ResultSerializer


def get_free_time(request, pk: int):
    date = request.GET.get('date', now().strftime('%Y-%m-%d'))
    _now = datetime.strptime(date, '%Y-%m-%d')
    _start = copy(_now).replace(hour=9)
    _end = copy(_now).replace(hour=18)

    free_time = []
    query_set = Book.objects.filter(
        start__date=date, room_id=pk
    )

    if query_set:
        _first = query_set[0].start

        if not (_first.hour == _now.hour and _first.minute == _now.minute):
            free_time.append({
                'start': _start,
                'end': _first
            })

    for i, book in enumerate(query_set, 1):
        if book.start > query_set[i - 1].start:
            free_time.append({
                'start': book.start,
                'end': query_set[i - 1].end
            })
    else:
        if query_set:
            _last = query_set.last().end
            if not (_end.hour == _now.hour and _end.minute == _now.minute):
                free_time.append({
                    'start': _last,
                    'end': _end
                })
        else:
            free_time.append({
                'start': _start,
                'end ': _end
            })
    return ResultSerializer(free_time, many=True).data
