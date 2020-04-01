import uuid
from django.db import models

class Template(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField()
    overlays = models.TextField()

    def __str__(self):
        return self.name


class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tokens = models.TextField()

    def __str__(self):
        return self.tokens


class Effect(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    effects = models.TextField()

    def __str__(self):
        return self.effects


class Stream(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    stream_key = models.TextField()
    process_ids = models.TextField()

    def __str__(self):
        return 'Stream key: {}\nProcess IDs: {}'.format(self.stream_key, self.process_ids)
