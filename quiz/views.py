from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views import View
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import json

from . models import *
from . forms import *
from accounts.models import User
from .mixins import *

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


@method_decorator(login_required, name='dispatch')
class QuizHome(View):
    def get(self, request):

        return render(request, 'quiz/home.html')

@method_decorator(login_required, name='dispatch')
class QuizSelect(View):
    template_name = 'quiz/quizselect.html'
    model_mylevel = MyLevel.objects.all()

    def get(self, request):
        levels = self.model_mylevel.order_by('name')

        context = {'levels':levels}
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        level_val = data.get('levelValue')
        course_val = data.get('courseValue')

        if level_val:
            courses = MyCourse.objects.filter(level__name__startswith=level_val[0]).values('name', 'slug')

            return JsonResponse({'courses': list(courses)})
        if json.loads(request.body)['courseValue']:
            # For the quiz display on course click
            course_value = json.loads(request.body)['courseValue']
            print(f'course value: {course_value}')
            
            if course_value in MyCourse.objects.name:
                questions = MyCourse.objects.all()
                
                context = {'questions': questions}
                return redirect('quiz', context)
            return JsonResponse(context, safe=False)

class Quiz(LoginRequiredMixin, ListView):
    model = Question
    template_name = 'quiz/quiz.html'
    paginate_by = 1  
    context_object_name = 'questions'  

    def get_queryset(self):
        return Question.objects.filter(course__slug=self.kwargs.get('course_slug'))


    # def get(self, request):
    #     print('user group = ' + str(request.user.groups.all()))

    #     data_list = Question.objects.all()
    #     page = request.GET.get('page', 1)

    #     paginator = Paginator(data_list, 1)

    #     try:
    #         data = paginator.page(page)
    #     except PageNotAnInteger:
    #         data = paginator.page(1)
    #     except EmptyPage:
    #         data = paginator.page(paginator.num_pages)

    #     form = self.form_name
        
    #     context = {'data':data, 'form':form}
    #     return render(request, self.template_name, context)

    # def post(self, request):
    #     template_name = 'quiz/quiz.html'
    #     form_data = request.POST.get('option')
    #     score = 0

    #     if form_data == 'c':
    #         score + 1
    #     elif form_data != 'c':
    #         score = score
        
    #     context = {'score':score}
    #     return render(request, self.template_name, context)
        
            
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