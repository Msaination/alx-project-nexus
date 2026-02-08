# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin
# from .models import User

# class CustomUserAdmin(UserAdmin):
#     model = User
#     list_display = ['username', 'email', 'first_name', 'last_name', 'role', 'is_staff']
#     fieldsets = UserAdmin.fieldsets + (
#         (None, {'fields': ('role',)}),
#     )


# admin.site.register(User, CustomUserAdmin)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    # Fields to display in the list view
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active', 'groups')

    # Fields to search
    search_fields = ('username', 'email', 'first_name', 'last_name')

    # Fieldsets for editing user details
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'role')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    # Fields for creating a new user in admin
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'role', 'password1', 'password2'),
        }),
    )

    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions',) 