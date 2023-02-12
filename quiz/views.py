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

        if level_val:
            courses = MyCourse.objects.filter(level__name__startswith=level_val[0]).values('name', 'slug')

            return JsonResponse({'courses': list(courses)})

class Quiz(LoginRequiredMixin, ListView):
    model = Question
    template_name = 'quiz/quiz.html'
    paginate_by = 1  
    context_object_name = 'questions'

    def get_queryset(self):
        return Question.objects.filter(course__slug=self.kwargs.get('course_slug'))

    def post(self, request, *args, **kwargs):
        optionValue = request.POST.get('option')
        print('incoming post request')

        score = 0
        page_number = int(self.request.GET.get('page'))

        if optionValue.upper() == self.model.objects.all()[page_number-1].answer:
            score += 1
            print(f'Score: {score}')
        else:
            pass

        context = {'score':score}
        return JsonResponse(context, safe=False)

# JSON RESPONSE
def JsonRes(self, request, *args, **kwargs):
    if request.method == 'POST':
        print("\nIT'S WORKING")

        optionValue = request.POST.get('option')
        context = {'data': optionValue}

        return JsonResponse(context)
#**************************************************#
            
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