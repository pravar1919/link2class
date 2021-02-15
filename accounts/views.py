from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout,get_user_model
from django.contrib.auth import login as auth_login
from django.contrib import messages
from .models import CustomUser, Profile
from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth.views import PasswordChangeView, PasswordResetDoneView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .forms import  LoginForm, RegisterForm, ProfileUpdateForm, UserUpdateForm

# Create your views here.
User = get_user_model()

def login(request):
    form =  LoginForm(request.POST or None)
    form_r =  RegisterForm(request.POST or None)
    context = {
        'form':form,
        'form_r':form_r,
    }
    if form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            return JsonResponse({"error": form.errors}, status=400)
    else:
        return render(request, 'accounts/login.html', context)


def register(request):
    form =  RegisterForm(request.POST or None)
    context = {
        'form':form
    }
    if form.is_valid():
        first_name = form.cleaned_data.get('first_name')
        last_name = form.cleaned_data.get('last_name')
        email = form.cleaned_data.get('email')
        organization = form.cleaned_data.get('organization')
        title = form.cleaned_data.get('title')
        phone = form.cleaned_data.get('phone')
        share_my_contact = form.cleaned_data.get('share_my_contact')
        update_through_email = form.cleaned_data.get('update_through_email')
        password = form.cleaned_data.get('password')

        new_user = CustomUser.objects.create_user(first_name=first_name,last_name=last_name,phone=phone,email=email,organization=organization,title=title,share_my_contact=share_my_contact,update_through_email=update_through_email,password=password)
        new_user.save()
        auth_login(request,new_user)
        return redirect('home')
    return render(request, 'accounts/login.html',context)


@login_required
def logout(request):
    logout(request)
    return redirect("/")


class My_password_change(PasswordChangeView):
    template_name = 'training_center/home.html'
    success_url = reverse_lazy('accounts:password-change-done-view')


class My_password_reset_done(PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'
