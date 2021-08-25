from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _

User = get_user_model()


class UserAdmin(DjangoUserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password',)}),
        (_('Personal info'), {
         'fields': ('first_name', 'last_name', 'email', 'profile_image',)}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions',),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined',)}),
    )
    ordering = ('email',)


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
