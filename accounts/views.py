from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LogoutView
from django.views import View
from django.contrib.auth.models import Group

from . forms import RegisterForm
import sweetify
from django.contrib import messages

class RegisterView(View):
    def get(self, request):
        form = RegisterForm()

        return render(request, 'accounts/signup.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            group, created = Group.objects.get_or_create(name='user')
            user.groups.add(group)

            lastname = form.cleaned_data.get('last_name')
            messages.success(request, 'Account created for ' + lastname)
            
            return redirect(reverse('signin'))
        # print(form.errors())
        return redirect(reverse('signup'))

        

class LoginView(View):
    def get(self, request):

        return render(request, 'accounts/signin.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password1')

        user = authenticate(request, username=email, password=password)
        if user is not None:
            # if user.is_email_verified == False:
            #     sweetify.error(request, title="Not Verified", text="Please check your email for verification link", button="Ok", timer=3500)
            #     return redirect(reverse('signin'))
            login(request, user)
            return redirect(reverse('home'))
        sweetify.error(request, title="Invalid Credentials", text="Your email or password is incorrect", button="Ok", timer=3500)
        messages.error(request, 'Error: Email or Password incorrect!!')
        return redirect(reverse('signin'))
        
class MyLogoutView(LogoutView):
    next_page = '/accounts/signin'

class Lorem(View):
    def get(self, request):

        return render(request, 'accounts/lorem.html')