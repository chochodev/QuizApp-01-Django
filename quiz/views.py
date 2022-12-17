from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from . models import *

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class QuizHome(View):
    def get(self, request):

        return render(request, 'quiz/home.html')


class QuizSelect(View):
    def get(self, request):

        return render(request, 'quiz/quizselect.html')


class Quiz(View):
    def get(self, request):
        data_list = Database.objects.all()
        page = request.GET.get('page', 1)

        paginator = Paginator(data_list, 1)

        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
        
        context = {'data':data}
        return render(request, 'quiz/quiz.html', context)


class QuizSettings(View):
    def get(self, request):

        return render(request, 'quiz/settings.html')


class QuizAbout(View):
    def get(self, request):

        return render(request, 'quiz/about.html')


class QuizNotification(View):
    def get(self, request):

        return render(request, 'quiz/notification.html')