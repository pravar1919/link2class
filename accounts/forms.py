from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, CustomUser
import math
from django.contrib.auth import get_user_model

User = get_user_model()


class LoginForm(forms.Form):
    email = forms.CharField(label="",widget=forms.TextInput(attrs={"class":"form-control","id":"login_mail"}))
    password = forms.CharField(label="",widget=forms.PasswordInput(attrs={"class":"form-control","id":"login_password"}))


class RegisterForm(forms.Form):
    STATUS_CHOICES = (
        ('','Status'),
        ('active duty','Active Duty'),
        ('guard/reserve','Gurad/Reserve'),
        ('veteran','Veteran'),
        ('retired','Retired'),
        ('spouse','Spouse'),
    )
    ORGANIZATION_CHOICES = (
        ('','Organization'),
        ('air force','Air Force'),
        ('army','Army'),
        ('coast guard','Coast Guard'),
        ('marine corps','Marine Corps'),
        ('navy','Navy'),
    )
    RANK_CHOICES = (
        ('','Rank'),
        ('e1','E-1'),
        ('e2','E-2'),
        ('e3','E-3'),
        ('e4','E-4'),
        ('e5','E-5'),
        ('e6','E-6'),
        ('e7','E-7'),
        ('e8','E-8'),
        ('e9','E-9'),
    )

    first_name = forms.CharField(label="",widget=forms.TextInput(attrs={"class":"form-control","placeholder":"First Name","id":"reg_first_name"}))
    last_name = forms.CharField(label="",widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Last Name","id":"reg_last_name"}))
    email = forms.EmailField(label="",widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"Email","id":"reg_email"}))
    password = forms.CharField(label="",widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Password","id":"reg_password"}))
    password2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Confirm Password","id":"reg_password2"}))
    organization = forms.ChoiceField(label="",choices = ORGANIZATION_CHOICES)
    rank = forms.ChoiceField(label="",choices = RANK_CHOICES)
    current_status = forms.ChoiceField(label="",choices = STATUS_CHOICES)
    date_of_sepration = forms.DateField(widget=forms.DateInput(attrs={"class":"form-control",'type': 'date'}))
    phone = forms.CharField(label="",widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Mobile Number","id":"reg_phone"}))
    share_my_contact = forms.BooleanField(required=False,widget=forms.CheckboxInput())
    update_through_email = forms.BooleanField(required=False,widget=forms.CheckboxInput())

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password2 != password:
            raise forms.ValidationError('Password Does not match!!')
        return data   
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = CustomUser.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('Email is Taken')
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if len(phone)<10 and math.isnan(phone):
            raise forms.ValidationError("Phone should be a 10 digit number.")
        return phone



class ProfileUpdateForm(forms.ModelForm):
    address = forms.CharField(required=False, max_length=500)
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

