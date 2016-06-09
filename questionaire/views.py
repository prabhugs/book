from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .models import Question, Choice, Student, Exam


# Create your views here.
@login_required
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    this_student = get_object_or_404(Student, user_id=request.user.id)
    my_question_list = Question.objects.filter(level=this_student.current_level_id)

    print request.user.id, request.user, request.user.username, this_student.current_level_id, this_student.current_level

    test_list = Exam.objects.filter(assigned_to=this_student.id, status='O')
    print test_list

    template = loader.get_template("questionaire/index.html")
    context = {'latest_question_list': latest_question_list,
               'my_question_list' : my_question_list,
               'student' : this_student,
               'test_list': test_list,}

    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    #try:
    #    question = Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
    #    raise Http404("Question does NOT exist")
    #return HttpResponse("You're looking at question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'questionaire/detail.html', {'question': question})

def test(request, test_id):
    test = get_object_or_404(Exam, pk=test_id)
    print test.id, test, test.question.all()
    this_student = get_object_or_404(Student, user_id=request.user.id)
    return render(request, 'questionaire/test.html', {'test': test, 'student' : this_student})

def results(request, question_id):
    #response = "You're looking at the results of question %s."
    #return HttpResponse(response % question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'questionaire/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
	selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
	return render(request, 'questionaire/detail.html', {'question': question, 'error_message': "Please select an answer"})
    else:
	selected_choice.votes += 1
	selected_choice.save()
	return HttpResponseRedirect(reverse('questionaire:results', args=(question_id,)))

#from django.shortcuts import render_to_response
#from django.template import RequestContext

#from .forms import UploadFileForm 

#def list(request):
#    # Handle file upload
#    if request.method == 'POST':
#        form = UploadFileForm(request.POST, request.FILES)
#        if form.is_valid():
#            newdoc = Question(docfile = request.FILES['docfile'])
#            newdoc.save()

            # Redirect to the document list after POST
#            return HttpResponseRedirect(reverse('questionaire.views.list'))
#    else:
#        form = UploadFileForm() # A empty, unbound form

    # Load documents for the list page
#    documents = Question.objects.all()

    # Render list page with the documents and the form
#    return render_to_response(
#        'questionaire/list.html',
#        {'documents': documents, 'form': form},
#        context_instance=RequestContext(request)
#    )
