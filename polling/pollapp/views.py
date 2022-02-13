from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from pollapp.models import Questions, Answer, ChoiseVoit, ChoisePoll
from pollapp.forms import ChoisePollCreateForm
# Create your views here.


def poll(request):
    title = 'Опросник'
    questions_list = Questions.objects.all()
    answer_list = Answer.objects.all()

    if request.method == 'POST':
        choise_voit_form = ChoisePollCreateForm(request.POST, request.FILES)

        if choise_voit_form.is_valid():
            choise_voit_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
    else:
        choise_poll_form = ChoisePollCreateForm()

    content = {
        'title': title,
        'questions_list': questions_list,
        'answer_list': answer_list,
        'choise_poll_form': choise_poll_form
    }

    return render(request, 'pollapp/poll.html', content)


def quest(request):
    title = 'Создание вопроса'

    content = {
        'title': title,
    }

    return render(request, 'pollapp/questions.html', content)

