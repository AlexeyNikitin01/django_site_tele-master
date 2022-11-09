from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from .forms import UserSignUpForm, UserSignInForm


class UserSignUpView(View):
    def get(self, request, *args, **kwargs):
        form = UserSignUpForm()
        context = {
            'form': form,
        }
        return render(request, 'main/tm_user/register_user.html', context=context)

    def post(self, request, *args, **kwargs):
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
                return redirect('/')
        context = {
            'form': form,
        }
        return render(request, 'main/tm_user/register_user.html', context=context)


class UserSignInView(View):
    def get(self, request, *args, **kwargs):
        form = UserSignInForm()
        context = {
            'form': form,
        }
        return render(request, 'main/tm_user/login.html', context)

    def post(self, request, *args, **kwargs):
        form = UserSignInForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
        context = {
            'form': form,
        }
        return render(request, 'main/tm_user/login.html', context)


class LogOut(LogoutView):
    template_name = 'main/tm_user/logout.html'


@login_required
def profile(request):
    return render(request, template_name='main/tm_user/profile.html')


class RegisterDone(TemplateView):
    template_name = 'main/tm_user/register_done.html'


