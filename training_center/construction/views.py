from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Construction
from django.contrib.auth.decorators import login_required
from accounts.forms import  LoginForm, RegisterForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.

@login_required
def construction(request):
    form = PasswordChangeForm(request.user, request.POST or None)
    u_form = UserUpdateForm(request.POST, instance=request.user)
    p_form = ProfileUpdateForm(request.POST,
                               request.FILES,
                               instance=request.user.profile)
    if form.is_valid():
        form.save()
        return redirect('accounts:password-change-done-view')
    
    if u_form.is_valid() and p_form.is_valid():
        u_form.save()
        p_form.save()
        
        messages.success(request, f'Your account has been updated!')
        return redirect('/')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    qs = Construction.objects.all()
    context = {
        'qs':qs,
        'u_form': u_form,
        'p_form': p_form,
        'name':'construction',
        'form':form
    }
    return render(request,'training_center/home.html',context)

@login_required
def todays_events_view(request, pk):
    qs = Construction.objects.get(id=pk)
    try:
        if not len(qs.todays_events) > 0:
            print("Not Found")
    except:
        return qs
    context = {
        'qs':qs,
        'name':'construction',
    }
    return render(request,'training_center/todays_events.html',context)

@login_required
def upcoming_events_view(request, pk):
    qs = Construction.objects.get(id=pk)
    print(qs.upcoming_events)
    try:
        if not len(qs.upcoming_events) > 0:
            print("Not Found")
    except:
        return qs
    context = {
        'qs':qs,
    }
    return render(request,'training_center/upcoming_events.html',context)



@login_required
def ondemand_events_view(request, pk):
    qs = Construction.objects.get(id=pk)
    # print(qs.ondemand_events)
    try:
        if not len(qs.ondemand_events) > 0:
            print("Not Found")
    except:
        return qs
    context = {
        'qs':qs,
    }
    return render(request,'training_center/ondemand_events.html',context)

