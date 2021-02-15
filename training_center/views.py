# from django.shortcuts import render,redirect
# from django.contrib import messages
# from .models import TrainingCenter
# from django.contrib.auth.decorators import login_required
# from accounts.forms import  LoginForm, RegisterForm, ProfileUpdateForm, UserUpdateForm

# Create your views here.

# @login_required
# def construction(request):
#     u_form = UserUpdateForm(request.POST, instance=request.user)
#     p_form = ProfileUpdateForm(request.POST,
#                                request.FILES,
#                                instance=request.user.profile)
#     if u_form.is_valid() and p_form.is_valid():
#         u_form.save()
#         p_form.save()
#         messages.success(request, f'Your account has been updated!')
#         return redirect('/')

#     else:
#         u_form = UserUpdateForm(instance=request.user)
#         p_form = ProfileUpdateForm(instance=request.user.profile)
#     qs = TrainingCenter.objects.filter(title='Construction')
#     if qs.exists():
#         first = qs.first()
#     context = {
#         'qs':first,
#         'u_form': u_form,
#         'p_form': p_form,
#     }
#     return render(request,'training_center/home.html',context)

# @login_required
# def transportation(request):
#     u_form = UserUpdateForm(request.POST, instance=request.user)
#     p_form = ProfileUpdateForm(request.POST,
#                                request.FILES,
#                                instance=request.user.profile)
#     if u_form.is_valid() and p_form.is_valid():
#         u_form.save()
#         p_form.save()
#         messages.success(request, f'Your account has been updated!')
#         return redirect('/')

#     else:
#         u_form = UserUpdateForm(instance=request.user)
#         p_form = ProfileUpdateForm(instance=request.user.profile)

#     qs = TrainingCenter.objects.filter(title='Transportation')
#     if qs.exists():
#         first = qs.first()
#     context = {
#         'qs':first,
#         'u_form': u_form,
#         'p_form': p_form,
#     }
#     return render(request,'training_center/home.html',context)

# @login_required
# def manufacturing(request):
#     u_form = UserUpdateForm(request.POST, instance=request.user)
#     p_form = ProfileUpdateForm(request.POST,
#                                request.FILES,
#                                instance=request.user.profile)
#     if u_form.is_valid() and p_form.is_valid():
#         u_form.save()
#         p_form.save()
#         messages.success(request, f'Your account has been updated!')
#         return redirect('/')

#     else:
#         u_form = UserUpdateForm(instance=request.user)
#         p_form = ProfileUpdateForm(instance=request.user.profile)
#     qs = TrainingCenter.objects.filter(title='Manufacturing')
#     if qs.exists():
#         first = qs.first()
#     context = {
#         'qs':first,
#         'u_form': u_form,
#         'p_form': p_form,
#     }
#     return render(request,'training_center/home.html',context)

# @login_required
# def health_and_medicine(request):
#     u_form = UserUpdateForm(request.POST, instance=request.user)
#     p_form = ProfileUpdateForm(request.POST,
#                                request.FILES,
#                                instance=request.user.profile)
#     if u_form.is_valid() and p_form.is_valid():
#         u_form.save()
#         p_form.save()
#         messages.success(request, f'Your account has been updated!')
#         return redirect('/')

#     else:
#         u_form = UserUpdateForm(instance=request.user)
#         p_form = ProfileUpdateForm(instance=request.user.profile)
#     qs = TrainingCenter.objects.filter(title='HealthCare')
#     if qs.exists():
#         first = qs.first()
#     context = {
#         'qs':first,
#         'u_form': u_form,
#         'p_form': p_form,
#     }
#     return render(request,'training_center/home.html',context)

# @login_required
# def marketing(request):
#     u_form = UserUpdateForm(request.POST, instance=request.user)
#     p_form = ProfileUpdateForm(request.POST,
#                                request.FILES,
#                                instance=request.user.profile)
#     if u_form.is_valid() and p_form.is_valid():
#         u_form.save()
#         p_form.save()
#         messages.success(request, f'Your account has been updated!')
#         return redirect('/')

#     else:
#         u_form = UserUpdateForm(instance=request.user)
#         p_form = ProfileUpdateForm(instance=request.user.profile)
#     qs = TrainingCenter.objects.filter(title='Marketing')
#     if qs.exists():
#         first = qs.first()
#     context = {
#         'qs':first,
#         'u_form': u_form,
#         'p_form': p_form,
#     }
#     return render(request,'training_center/home.html',context)

# @login_required
# def information_tech(request):
#     u_form = UserUpdateForm(request.POST, instance=request.user)
#     p_form = ProfileUpdateForm(request.POST,
#                                request.FILES,
#                                instance=request.user.profile)
#     if u_form.is_valid() and p_form.is_valid():
#         u_form.save()
#         p_form.save()
#         messages.success(request, f'Your account has been updated!')
#         return redirect('/')

#     else:
#         u_form = UserUpdateForm(instance=request.user)
#         p_form = ProfileUpdateForm(instance=request.user.profile)
#     qs = TrainingCenter.objects.filter(title='InformationTechnology')
#     if qs.exists():
#         first = qs.first()
#     context = {
#         'qs':first,
#         'u_form': u_form,
#         'p_form': p_form,
#     }
#     return render(request,'training_center/home.html',context)


# @login_required
# def profile(request):
#     u_form = UserUpdateForm(request.POST, instance=request.user)
#     p_form = ProfileUpdateForm(request.POST,
#                                request.FILES,
#                                instance=request.user.profile)
#     if u_form.is_valid() and p_form.is_valid():
#         u_form.save()
#         p_form.save()
#         messages.success(request, f'Your account has been updated!')
#         return redirect('main_user:profile')

#     else:
#         u_form = UserUpdateForm(instance=request.user)
#         p_form = ProfileUpdateForm(instance=request.user.profile)

#     context = {
#         'u_form': u_form,
#         'p_form': p_form,
#     }

#     return render(request, 'training_center/pf.html', context)