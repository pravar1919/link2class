from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Career, Like
from accounts.models import CustomUser
from django.contrib.auth.decorators import login_required
from accounts.forms import  LoginForm, RegisterForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.forms import PasswordChangeForm




@login_required
def information_tech(request):
    profile = CustomUser.objects.get(first_name=request.user.first_name)
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
    qs = Career.objects.all()
    context = {
        'qs':qs,
        'u_form': u_form,
        'p_form': p_form,
        'form':form,
        'profile':profile
    }
    return render(request,'training_center/home.html',context)

@login_required
def todays_events_view(request, pk):
    qs = Career.objects.get(id=pk)
    try:
        if not len(qs.todays_events) > 0:
            print("Not Found")
    except:
        return qs
    context = {
        'qs':qs,
    }
    return render(request,'training_center/todays_events.html',context)

@login_required
def upcoming_events_view(request, pk):
    qs = Career.objects.get(id=pk)
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
    qs = Career.objects.get(id=pk)
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


def like_unlike_post_career(request):
    user = request.user.first_name
    # print("********************",user)
    # if not request.method == 'POST' or user.is_authenticated:
    post_id = request.POST.get('post_id')
    # print('post_id ', post_id)
    post_obj = Career.objects.get(id=post_id)
    profile = CustomUser.objects.get(first_name=user)
    if profile in post_obj.liked.all():
        a = post_obj.liked.remove(profile)
    else:
        post_obj.liked.add(profile)

    like, created = Like.objects.get_or_create(
        user=profile, post_id=post_id)

    if not created:
        if like.value == 'Like':
            like.value = 'Unlike'
        else:
            like.value = 'Like'
    else:
        like.value = 'Like'

    post_obj.save()
    like.save()
    # else:
    #     messages.error(
    #         request, f'PLease login to continue')
    #     return HttpResponseRedirect('accounts:login_page')

    return redirect('/')