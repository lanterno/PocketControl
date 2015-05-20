from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from .models import User
from users.admin import UserAdmin


class UserAdmin(UserAdmin):
    list_filter = ('is_active',)
    fieldsets = (
        (None, {
            'fields': ('email', 'password')
        }),
        (_('Status'), {
            'fields': ('is_active',)
        }),
        (_('Personal Information'), {
            'fields': ('full_name', 'avatar'),
        }),
        (_('Important dates'), {
            'fields': ('last_login', 'date_joined')
        }),
    )

admin.site.register(User, UserAdmin)
