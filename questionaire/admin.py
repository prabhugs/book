from django.contrib import admin
from .models import Question, Choice, Level
from django.db import models

# Register your models here.
class Image(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media/documents")

class InlineImage(admin.TabularInline):
    model = Image

class QuestionAdmin(admin.ModelAdmin):
    inlines = [InlineImage]

#admin.site.register(Question, QuestionAdmin)

admin.site.register(Level)
admin.site.register(Question)
admin.site.register(Choice)
