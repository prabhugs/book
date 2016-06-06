from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import User

class Level(models.Model):
    level_text = models.CharField(max_length=10)

    def __str__(self):
        return self.level_text

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    current_level = models.ForeignKey(Level)
    #completed_levels = models.ManyToManyField(Level)
    last_visited = models.DateTimeField("last visited")

class Progress(models.Model):
    author = models.ForeignKey(Student, on_delete=models.CASCADE)
    level = models.ForeignKey(Level)
    completed = models.BooleanField(default=False)
    score = models.IntegerField(default=0)

# Create your models here.
class Question(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    question_text = models.CharField(max_length = 100)
    #docfile4 = models.FileField(upload_to='images')
    pub_date = models.DateTimeField("published date")

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length = 200)
    docfile = models.FileField(upload_to='images')
    is_answer = models.BooleanField(default=False)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Choice, on_delete=models.CASCADE)
    author = models.ForeignKey(Student, on_delete=models.CASCADE)
    answered_on = models.DateTimeField("answered on")
    #attempt = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
