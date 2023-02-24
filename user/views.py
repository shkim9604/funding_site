from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views import View


# Create your views here.

def index(request):
    return render(request, 'base.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return render(request, 'login.html', {'error': '이메일이 존재하지 않습니다.'})
        user = authenticate(request, user_mail=user.email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error': '이메일 또는 비밀번호가 올바르지 않습니다.'})


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')
