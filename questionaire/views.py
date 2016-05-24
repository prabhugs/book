from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .models import Question, Choice


# Create your views here.
@login_required
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template("questionaire/index.html")
    context = {'latest_question_list': latest_question_list, }
    #output = ','.join([q.question_text for q in latest_question_list])
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    #try:
    #    question = Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
    #    raise Http404("Question does NOT exist")
    #return HttpResponse("You're looking at question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'questionaire/detail.html', {'question': question})

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
	return render(request, 'questionaire/detail.html', {'question': question, 'error_message': "Choice not selected"})
    else:
	selected_choice.votes += 1
	selected_choice.save()
	return HttpResponseRedirect(reverse('questionaire:results', args=(question_id,)))

