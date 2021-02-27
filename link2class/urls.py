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
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('benifits/',include('training_center.benifits.urls'),name='const'),
    path('healthcare/',include('training_center.healthcare.urls'),name='healthcare'),
    path('career/',include('training_center.career.urls'),name='info_tech'),
    path('familysupport/',include('training_center.familysupport.urls'),name='manufacturing'),
    path('peer2peer/',include('training_center.peer2peer.urls'),name='marketing'),
    path('transition/',include('training_center.transition.urls'),name='trans'),
    path('password-reset/', auth_views.PasswordResetView.as_view(
         template_name='accounts/password_reset.html'), name='password_reset'),
    path('msg/',views.message_send, name='msg_sent'),         
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


admin.site.site_header = 'Link2Class Dashboard'
admin.site.site_title = "Admin Portal"
admin.site.index_title = 'Link2Class Administration'
