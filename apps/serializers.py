from datetime import datetime

from django.db.models import Q
from rest_framework.exceptions import ValidationError
from rest_framework.fields import JSONField
from rest_framework.serializers import ModelSerializer, DateTimeField, Serializer

from apps.models import Room, Book, Resident


class RoomModelSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'name', 'type', 'capacity')


class BookModelSerializer(ModelSerializer):
    resident = JSONField(write_only=True)
    start = DateTimeField()
    end = DateTimeField()

    def validate(self, attrs):
        start = attrs.get('start')
        end = attrs.get('end')
        _range = (start, end)

        _start = datetime(year=start.year, month=start.month, day=start.day, hour=9)
        _end = datetime(year=end.year, month=end.month, day=end.day, hour=18)

        if start >= end or start.date() != end.date() or start < _start or end > _end:
            raise ValidationError()

        if Book.objects.filter(Q(start__range=_range) | Q(end__range=_range)).exists():
            raise ValidationError()

        return super().validate(attrs)

    def create(self, validated_data):
        data = validated_data.pop('resident')
        resident = Resident.objects.create(**data)
        book = super().create(validated_data | {'resident_id': resident.id})
        return book

    class Meta:
        model = Book
        fields = ('resident', 'start', 'end')


class ResultSerializer(Serializer):
    start = DateTimeField()
    end = DateTimeField()
