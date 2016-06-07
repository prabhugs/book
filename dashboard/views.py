from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from questionaire.models import Student, Question

# Create your views here.
def index(request):
    if request.user.id:
        this_student = get_object_or_404(Student, pk=request.user.id)
        return render(request, 'dashboard/index.html', {'student' : this_student})
    else:
        return render(request, 'dashboard/index.html')
