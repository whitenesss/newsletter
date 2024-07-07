from django.contrib import admin

from blog.models import Blog


# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'image', 'created_at', 'count_view')
    list_filter = ('title', 'created_at', 'count_view')
    search_fields = ('title', 'content')
