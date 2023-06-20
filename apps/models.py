from django.db.models import Model, CharField, IntegerField, TextChoices, ForeignKey, CASCADE, DateTimeField, \
    CheckConstraint


class Room(Model):
    class Type(TextChoices):
        FOCUS = 'focus', 'Focus'
        TEAM = 'team', 'Team'
        CONFERENCE = 'conference', 'Conference'

    name = CharField(max_length=255)
    type = CharField(max_length=25, choices=Type.choices)
    capacity = IntegerField()


class Resident(Model):
    name = CharField(max_length=55)


class Book(Model):
    room = ForeignKey('apps.Room', CASCADE)
    resident = ForeignKey('apps.Resident', CASCADE)
    start = DateTimeField()
    end = DateTimeField()

    class Meta:
        ordering = ('start',)
