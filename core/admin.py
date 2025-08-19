from django.contrib import admin

from .models import CostumeUser


@admin.register(CostumeUser)
class CostumeUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')
    search_fields = ('username', 'email')
    list_filter = ('username', 'email')
    # fieldsets = (
    #     (None, {'fields': ('username', 'email')}),
    #     ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',)}),
    # )