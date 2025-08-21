from django.contrib import admin

from .models import Recipe, Tag, Customer, Comment


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_public', 'is_active', 'difficulty',)
    list_per_page = 10
    list_editable = ('is_active', 'difficulty',)
    list_display_links = ('title',)
    search_fields = ('title', 'is_public', 'difficulty',)
    prepopulated_fields = {
        'slug': ('title',),
    }


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('__str__','joined_at')
    list_display_links = ('__str__',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author','name','created_at')
    list_display_links = ('name',)
