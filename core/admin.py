from django.contrib import admin

from core.models import (
    Contact,
    Subscribe,
)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'email', 'company', 'telephone')
    list_filter = ('created_at',)
    search_fields = ('first_name', 'email')

@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active', 'created_at',)
    list_filter = ('is_active',)
    search_fields = ('email',)
