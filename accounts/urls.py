from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.RegisterView.as_view(), name='signup'),
    path('signin/', views.LoginView.as_view(), name='signin'),
    path('signout/', views.MyLogoutView.as_view(), name='signout'),
    path('lorem/', views.Lorem.as_view(), name='lorem'),
    
]