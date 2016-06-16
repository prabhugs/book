from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from questionaire.models import Student, Question, Answer

from django.db.models import Sum

# Create your views here.
def index(request):
    if request.user.id:
        this_student = get_object_or_404(Student, user_id=request.user.id)
        this_student_total_score = Answer.objects.filter(student=this_student).aggregate(total=Sum('score'))['total']
        return render(request, 'dashboard/index.html', {'student' : this_student, 'score' : this_student_total_score})
    else:
        return render(request, 'dashboard/index.html')
