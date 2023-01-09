from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from . models import *
from . forms import *
from accounts.models import User
from . decorators import *

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@method_decorator(login_required, name='dispatch')
class QuizHome(View):
    def get(self, request):

        return render(request, 'quiz/home.html')

@method_decorator(login_required, name='dispatch')
class QuizSelect(View):
    template_name = 'quiz/quizselect.html'

    def get(self, request):
        level = MyLevel.objects.all()
        courses = MyCourse.objects.all()

        context = {'level':level, 'courses':courses}
        return render(request, self.template_name, context)
    
    def post(self, request):
        
        context = {}
        return render(request, self.template_name, context)

@method_decorator(login_required, name='dispatch')
@method_decorator(allowed_users(['user', 'admin']), name='dispatch')
class Quiz(View):
    template_name = 'quiz/quiz.html'
    form_name = QuizForm

    def get(self, request):
        print('user group = ' + str(request.user.groups.all()))

        data_list = Question.objects.all()
        page = request.GET.get('page', 1)

        paginator = Paginator(data_list, 1)

        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)

        form = self.form_name
        
        context = {'data':data, 'form':form}
        return render(request, self.template_name, context)

    def post(self, request):
        template_name = 'quiz/quiz.html'
        form_data = request.POST.get('option')
        score = 0

        if form_data == 'c':
            score + 1
        elif form_data != 'c':
            score = score
        
        context = {'score':score}
        return render(request, self.template_name, context)
        
            
@method_decorator(login_required, name='dispatch')
class QuizSettings(View):
    template_name = 'quiz/settings.html'
    form_name = SettingsForm

    def get(self, request):

        return render(request, self.template_name)

    def post(self, request):
        user = request.user
        form = self.form_name(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()

        context = {'form':form}
        return render(request, self.template_name, context)

@method_decorator(login_required, name='dispatch')
class QuizAbout(View):
    def get(self, request):

        return render(request, 'quiz/about.html')

@method_decorator(login_required, name='dispatch')
class QuizNotification(View):
    def get(self, request):

        return render(request, 'quiz/notification.html')