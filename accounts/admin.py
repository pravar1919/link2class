from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Profile

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('first_name', 'email', 'organization', 'title','phone', 'is_staff', 'is_active')
    list_filter = ('first_name', 'email', 'organization', 'title', 'phone', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('first_name', 'email','organization','title','share_my_contact', 'update_through_email', 'password',
                           'phone')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'organization', 'title','share_my_contact','update_through_email', 'phone', 'password1', 'password2', 'is_staff', 'is_active')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)

