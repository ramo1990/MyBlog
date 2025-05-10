from django.contrib import admin
from .models import Post, PostImage
# Register your models here.

class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'status', 'created_on')
    search_fields = ('title', 'content')
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)} # Le slug est généré automatiquement à partir du titre
    inlines = [PostImageInline]

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    list_display = ('post', 'image')

