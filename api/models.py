from django.db import models

class Overlay(models.Model):
    template = models.TextField()

    def __str__(self):
        return self.template