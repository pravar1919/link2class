from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

# from accounts import views as account_view
from . import views
from django.urls import path, include

urlpatterns = [
    path('',views.home, name='home'),
    # path('login/',account_view.login_page,name='login'),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('logout/',LogoutView.as_view(),name='logout'),
    # path('signup/',account_view.register_page,name='signup'),
    path('training_center/',include('training_center.urls'),name='ts'),
    path('construction/',include('training_center.construction.urls'),name='const'),
    path('healthcare/',include('training_center.healthcare.urls'),name='healthcare'),
    path('infotech/',include('training_center.info_tech.urls'),name='info_tech'),
    path('manufacturing/',include('training_center.manufacturing.urls'),name='manufacturing'),
    path('marketing/',include('training_center.marketing.urls'),name='marketing'),
    path('transportaion/',include('training_center.transportation.urls'),name='trans'),
    path('password-reset/', auth_views.PasswordResetView.as_view(
         template_name='accounts/password_reset.html'), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(
        template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset/done', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done_forget.html'), name='password_reset_done'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
    
    path('admin/', admin.site.urls),


]
if settings.DEBUG: 
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

