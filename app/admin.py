from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(SubCategory)
class SubCategoryAdmin(TranslationAdmin):
    list_display = ('title', 'category', 'slug')
    list_filter = ('category',)
    prepopulated_fields = {'slug': ('title',)}

@admin.register(GalleryImage)
class GalleryImageAdmin(TranslationAdmin):
    list_display = ('subcategory', 'caption', 'image')
    list_filter = ('subcategory',)

@admin.register(Lieu)
class LieuAdmin(TranslationAdmin):
    prepopulated_fields = {'slug':('nom',)}
    list_display = ('nom', 'slug', 'distance_km', 'duree')
    list_filter = ('distance_km',)
    search_fields = ('nom', 'description')

@admin.register(LieuShopping)
class LieuShoppingAdmin(TranslationAdmin):
    prepopulated_fields = {'slug':('nom',)}
    list_display = ('nom', 'type', 'region', 'date_ajout')
    search_fields = ('nom', 'description', 'region')
    list_filter = ('type', 'region')

@admin.register(Post)
class PostAdmin(TranslationAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('title' , 'slug' , 'status' , 'created_on')
    list_filter = ('status',)
    search_fields = ['title', 'content']

@admin.register(MoyenTransport)
class MoyenTransportAdmin(TranslationAdmin):
    list_display = ('nom', 'type', 'region', 'site_web', 'telephone')
    prepopulated_fields = {'slug': ('nom',)} # rempli le slug automatiquement
    list_filter = ('type', 'region')
    search_fields = ('nom', 'description', 'region')


@admin.register(Hebergement)
class HebergementAdmin(TranslationAdmin):
    list_display = ('title', 'slug', 'categorie')
    prepopulated_fields = {'slug': ('title',)}
# @admin.register(Hebergement)
# class HebergementAdmin(TranslationAdmin):
#     pass

@admin.register(Restaurant)
class RestaurantAdmin(TranslationAdmin):
    list_display = ('title', 'slug', 'categorie')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(InfoPratique)
class InfoPratiqueAdmin(TranslationAdmin):
    list_display = ('icon', 'title')

@admin.register(Sortie)
class SortieAdmin(TranslationAdmin):
    list_display = ('nom', 'type')
    prepopulated_fields = {'slug':('nom',)}

@admin.register(ActiviteLoisir)
class ActiviteLoisirAdmin(TranslationAdmin):
    list_display = ('nom', 'categorie', 'localisation', 'date_ajout')
    prepopulated_fields = {'slug':('nom',)}
    list_filter = ('categorie',)
    search_fields = ('nom', 'description', 'localisation')

admin.site.register(APropos)

