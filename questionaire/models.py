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

    def __str__(self):
        return self.user.username

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

class Exam(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    test_text = models.CharField(max_length=100)
    question = models.ManyToManyField(Question)
    total_score = models.IntegerField(default=30)
    student_score = models.IntegerField(default=0)
    assigned_to = models.ForeignKey(Student, on_delete=models.CASCADE)

    OPEN = 'O'
    STARTED = 'S'
    COMPLETED = 'C'
    INPROGRESS = 'P'
    status_choice = ((OPEN, "Open"), (STARTED, "Started"), (INPROGRESS, "In Progress"), (COMPLETED, "Completed"),)

    status = models.CharField(max_length = 1, choices=status_choice, default=OPEN)

    def __str__(self):
        return self.test_text

    def is_open(self):
        return self.status == self.OPEN

    def is_started(self):
        return self.status == self.STARTED

    def is_complete(self):
        return self.status == self.COMPLETED


