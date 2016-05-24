from __future__ import unicode_literals

import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Topic(models.Model):
    topic_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.topic_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - date.timedelta(days=1)


class Code(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    code_text = models.CharField(max_length=20000)
    answers = models.IntegerField(default=0)

    def __str__(self):
        return self.code_text

