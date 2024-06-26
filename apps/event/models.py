import uuid
from django.db import models

from apps.user.models import User


class Relative(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='relatives')
    name = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=128, unique=True)
    relationship = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='events')
    image = models.ImageField(upload_to='events/')
    title = models.CharField(max_length=128)
    description = models.TextField()

    def __str__(self):
        return self.title


class Vote(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='votes')
    relative = models.ForeignKey(Relative, on_delete=models.CASCADE, related_name='votes')
    type = models.BooleanField()

    class Meta:
        unique_together = ('event', 'relative')
