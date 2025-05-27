from django.contrib import admin
from .models import *

# class PostAdmin(admin.ModelAdmin):
#     list_display = ('title' , 'slug' , 'status' , 'created_on')
#     list_filter = ('status',)
#     search_fields = ['title', 'content']

class ImageSupplementaireInline(admin.TabularInline):
    model = ImageSupplementaire
    extra = 3 # nombre de formulaires vides par défaut
    fields = ['image', 'description']

class DestinationAdmin(admin.ModelAdmin):
    list_display = ['ville', 'slug']
    prepopulated_fields = {"slug": ("ville",)}
    inlines = [ImageSupplementaireInline]  # intègre les images

@admin.register(Culture)
class CultureAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('titre',)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('title' , 'slug' , 'status' , 'created_on')
    list_filter = ('status',)
    search_fields = ['title', 'content']

admin.site.register(VillePatrimoine)
admin.site.register(Gastronomie)
admin.site.register(Agenda)
admin.site.register(Destinations, DestinationAdmin)
admin.site.register(ConseilVoyage)
admin.site.register(APropos)

