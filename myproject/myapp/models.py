from django.db import models


class Project(models.Model):
    topic = models.CharField(max_length=100, default='')
    languages_used = models.CharField(max_length=100, default='')
    duration = models.IntegerField(default=0)

    def __str__(self):
        return self.topic
