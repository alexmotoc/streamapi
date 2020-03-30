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