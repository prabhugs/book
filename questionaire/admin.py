from django.contrib import admin
from .models import Question, Choice, Level, Student
from django.db import models
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

# Register your models here.
class Image(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media/documents")

class InlineImage(admin.TabularInline):
    model = Image

class QuestionAdmin(admin.ModelAdmin):
    inlines = [InlineImage]

class StudentInline(admin.StackedInline):
    model = Student
    can_delete = False
    verbose_name_plural = "students"

class StudentAdmin(UserAdmin):
    inlines = [StudentInline]

#admin.site.register(Question, QuestionAdmin)

admin.site.register(Level)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.unregister(User)
admin.site.register(User, StudentAdmin)
