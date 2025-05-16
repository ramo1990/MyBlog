from django.contrib import admin
from .models import *

class PostAdmin(admin.ModelAdmin):
    list_display = ('title' , 'slug' , 'status' , 'created_on')
    list_filter = ('status',)
    search_fields = ['title', 'content']

class ImageSupplementaireInline(admin.TabularInline):
    model = ImageSupplementaire
    extra = 3 # nombre de formulaires vides par défaut
    fields = ['image', 'description']

class DestinationAdmin(admin.ModelAdmin):
    list_display = ['ville', 'slug']
    prepopulated_fields = {"slug": ("ville",)}
    inlines = [ImageSupplementaireInline]  # intègre les images


admin.site.register(Post , PostAdmin)
admin.site.register(Destinations, DestinationAdmin)
admin.site.register(Culture)
admin.site.register(ConseilVoyage)
admin.site.register(MessageContact)
admin.site.register(APropos)
# Register your models here.

