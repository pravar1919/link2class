from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from accounts.forms import  LoginForm, RegisterForm, ProfileUpdateForm, UserUpdateForm
from django.contrib.auth.forms import PasswordChangeForm



@login_required#(login_url='/login/')
def home(request):
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
        # messages.success(request, f'Your account has been updated!')
        return redirect('/')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'form':form,
    }

    return render(request,'home.html',context)
    

def message_send(request):
    user = request.user
    if request.method=='POST':
        reciever = request.POST['reciever']
        subject = request.POST['subject']
        message = request.POST['message']
        message += f'''
                \n\nFrom: {user} \n\n To: {reciever}.
        '''
        res = send_mail(subject, message, "reboot@nvtsi.org", ['reboot@nvtsi.org'],fail_silently=False)
        # msg = SentMessage(reciever=reciever,sender=user,mesage=message,subject=subject)
        # msg.save()
        return redirect('/')