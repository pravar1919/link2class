from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, CustomUser
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","id":"login_mail"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","id":"login_password"}))


class RegisterForm(forms.Form):
    first_name = forms.CharField(label="",widget=forms.TextInput(attrs={"class":"form-control","placeholder":"First Name"}))
    last_name = forms.CharField(label="",widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Last Name"}))
    email = forms.EmailField(label="",widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"Email"}))
    password = forms.CharField(label="",widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password"}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Confirm Password"}))
    organization = forms.CharField(label="",widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Organization"}))
    title = forms.CharField(label="",widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Title"}))
    phone = forms.CharField(label="",widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Mobile Number"}))
    share_my_contact = forms.BooleanField(widget=forms.CheckboxInput())
    update_through_email = forms.BooleanField(widget=forms.CheckboxInput())
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = CustomUser.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('Email is Taken')
        return email



    # def clean(self):
    #     data = self.cleaned_data
    #     password = self.cleaned_data.get('password')
    #     password2 = self.cleaned_data.get('password2')
    #     if password2 != password:
    #         raise forms.ValidationError('Password Does not match!!')
    #     return data

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'address','state','city','zip_code', 'phone', 'image']
        # widgets = {
        #     'email': forms.EmailInput(attrs={'class': 'form-control', 'readonly': True}),
        # }


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'phone']
