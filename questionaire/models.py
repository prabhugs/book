from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Question(models.Model):

    question_text = models.CharField(max_length = 20)
    #docfile1 = models.FileField(upload_to='images')
    #docfile2 = models.FileField(upload_to='images')
    #docfile3 = models.FileField(upload_to='images')
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

#class Answer(models.Model):
#    question = models.ForeignKey(Question, on_delete=models.CASCADE)
#    answer = models.ForeignKey(Choice, on_delete=models.CASCADE)
