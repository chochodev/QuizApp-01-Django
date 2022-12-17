from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from . forms import RegisterForm
from django.contrib.auth import authenticate, login, logout
import sweetify

class RegisterView(View):
    def get(self, request):
        form = RegisterForm()

        return render(request, 'accounts/signup.html', {'form': form})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('login'))
        print(form.errors())
        return redirect(reverse('register'))

        

class LoginView(View):
    def get(self, request):
        form = RegisterForm()

        return render(request, 'accounts/signup.html', {'form': form})

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)
        if user is not None:
            if user.is_email_verified == False:
                sweetify.error(request, title="Not Verified", text="Please check your email for verification link", button="Ok", timer=3500)
                return redirect(reverse('login'))
            login(request, user)
            return redirect(reverse('home'))
        sweetify.error(request, title="Invalid Credentials", text="Your email or password is incorrect", button="Ok", timer=3500)
        return redirect(reverse('login'))
        