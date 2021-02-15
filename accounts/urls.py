from django.urls import path, include
from . import views


app_name = 'accounts'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('change-password/', views.My_password_change.as_view(),
         name='password-change-view'),
    path('change-password/done/', views.My_password_reset_done.as_view(),
         name='password-change-done-view'),
    
]
