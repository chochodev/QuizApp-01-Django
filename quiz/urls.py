from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.QuizHome.as_view(), name="home"),
    path('quizselect/', views.QuizSelect.as_view(), name="quizselect"),
    path('quiz/<slug:course_slug>/', views.Quiz.as_view(), name="quiz"),
    # JSON RESPONSE
    path('json/', views.JsonRes, name='json'),
    path('settings/', views.QuizSettings.as_view(), name="settings"),
    path('about/', views.QuizAbout.as_view(), name="about"),
    path('notification/', views.QuizNotification.as_view(), name="notification"),

]