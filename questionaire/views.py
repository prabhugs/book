from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from .models import Question, Choice, Student, Exam, Answer

from django.db.models import Sum

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
    this_student_score = Answer.objects.filter(student_id=this_student, test_id=test_id).aggregate(Sum('score'))['score__sum']
    if not this_student_score:
        this_student_score = 0
    answered_correctly_list = Answer.objects.filter(student_id=this_student, test_id=test_id, score__gt = 0)

    answered = {}
    for answer in answered_correctly_list:
        print "Anwered: ", answer.question_id, answer.score
        answered[answer.question_id] = answer.score
    return render(request, 'questionaire/test.html', {'test': test, 'student' : this_student, 'score': this_student_score, "answered": answered})

def results(request, question_id):
    #response = "You're looking at the results of question %s."
    #return HttpResponse(response % question_id)
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'questionaire/results.html', {'question': question})

def answer(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    selected_choice = None
    #print request.POST.get('choice', False)
    try:
	#selected_choice = question.choice_set.get(pk=request.POST['choice'])
	selected_choice = request.POST.get('choice', False)
        ##
        # TODO: Handle if choice not found
        ##
        selected_choice = Choice.objects.get(pk=selected_choice)
        #c = Choice.objects.get(pk=selected_choice)
        #print c.is_answer
    except (KeyError, Choice.DoesNotExist):
	return render(request, 'questionaire/detail.html', {'question': question, 'error_message': "Please select an answer"})
    else:
        this_student = get_object_or_404(Student, user_id=request.user.id)
        this_test = Exam.objects.filter(assigned_to=this_student.id, status='O')[0]
        #print this_student, question, selected_choice, this_test.student_score, this_test.total_score
        #print this_student, question, selected_choice, this_test.student_score, this_test.total_score
        this_score = 0

        if selected_choice.is_answer:

            previous_attempts = Answer.objects.filter(student = this_student, test = this_test, score = 0, question = question).count()

            if previous_attempts > 4:
                this_score = 0
            else:
                this_score = 1 - ((0.25) * previous_attempts)

            this_test.student_score += this_score
            this_test.save()

        #print "Score is :", this_score

        ans = Answer(test = this_test, question = question, answer = selected_choice, student = this_student, score = this_score)
        ans.save()

	return HttpResponseRedirect(reverse('questionaire:detail', args=(question_id,)))
	return HttpResponseRedirect(reverse('questionaire:results', args=(question_id,)))

