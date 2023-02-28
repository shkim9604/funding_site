from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth import authenticate, login
from django.views import View
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import User as f_User

# Create your views here.

def index(request):
    return render(request, 'base.html')


class LoginView(View):
    template_name = 'login.html'
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = f_User.objects.get(email=email)
            if check_password(password, user.password):
                request.session['user'] = user.id
                return redirect("/")
            else:
                return render(request, 'login.html', {'error': '비밀번호가 일치하지않습니다.'})
        except f_User.DoesNotExist:
            return render(request, 'login.html', {'error': '이메일이 존재하지 않습니다.'})



class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        name = request.POST.get('name')
        email = request.POST.get('Email')
        password = request.POST.get('password')
        re_password = request.POST.get('re-password')

        if password != re_password:
            return render(request, 'register.html', {'error': '비밀번호와 비밀번호 확인이 일치하지않습니다.'})
        else:
            user = f_User.objects.create(
                name=name,
                email=email,
                password=make_password(password)
            )
            return redirect("/login")
