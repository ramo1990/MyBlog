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

@admin.register(Hebergement)
class HebergementAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'categorie')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'categorie')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(InfoPratique)
class InfoPratiqueAdmin(admin.ModelAdmin):
    list_display = ('icon', 'title')

# Que faire ?
class ActiviteInline(admin.TabularInline):
    model = Activite
    extra = 1

@admin.register(CategorieActivite)
class CategorieActiviteAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon')
    inlines = [ActiviteInline]

@admin.register(Activite)
class ActiviteAdmin(admin.ModelAdmin):
    list_display = ('title', 'categorie')
    prepopulated_fields = {'slug':('title',)}

# @admin.register(CarouselSlide)
# class CarouselSlideAdmin(admin.ModelAdmin):
#     list_display = ('title', 'order', 'active')
#     list_editable = ['order', 'active']
######

admin.site.register(Destinations, DestinationAdmin)
admin.site.register(PlatTypique)
admin.site.register(APropos)

