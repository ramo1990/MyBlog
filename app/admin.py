from django.contrib import admin
from .models import *

class ImageSupplementaireInline(admin.TabularInline):
    model = ImageSupplementaire
    extra = 3 # nombre de formulaires vides par défaut
    fields = ['image', 'description']

class DestinationAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ImageSupplementaireInline]  # intègre les images

@admin.register(Culture)
class CultureAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ['title', 'slug']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('title' , 'slug' , 'status' , 'created_on')
    list_filter = ('status',)
    search_fields = ['title', 'content']

@admin.register(VillePatrimoine)
class VillePatrimoineAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'date')
    prepopulated_fields = {'slug': ('title',)} # rempli le slug automatiquement

@admin.register(Gastronomie)
class GastronomieAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'date')
    prepopulated_fields = {'slug': ('title',)} # rempli le slug automatiquement

@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'place')
    prepopulated_fields = {'slug': ('title',)} # rempli le slug automatiquement

@admin.register(ConseilVoyage)
class ConseilVoyageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'date')
    prepopulated_fields = {'slug': ('title',)} # rempli le slug automatiquement

admin.site.register(Destinations, DestinationAdmin)
# admin.site.register(ConseilVoyage)
admin.site.register(APropos)

