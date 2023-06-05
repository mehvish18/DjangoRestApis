from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserDetail


class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ('email', 'first_name', 'last_name', 'is_active', 'is_staff')
    ordering = ('email',)
    list_display = ('id', 'email', 'first_name', 'last_name', 'phone_number', 'is_active', 'is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
        ('Personal', {'fields': ('phone_number',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'last_name', 'phone_number', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser')}
         ),
    )

admin.site.register(UserDetail)
admin.site.register(User, UserAdminConfig)
