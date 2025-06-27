from django.contrib import admin
from .models import *

# class ImageSupplementaireInline(admin.TabularInline):
#     model = ImageSupplementaire
#     extra = 3 # nombre de formulaires vides par défaut
#     fields = ['image', 'description']

# class DestinationAdmin(admin.ModelAdmin):
#     list_display = ['title', 'slug']
#     prepopulated_fields = {"slug": ("title",)}
#     inlines = [ImageSupplementaireInline]  # intègre les images

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'slug')
    list_filter = ('category',)
    prepopulated_fields = {'slug': ('title',)}

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('subcategory', 'caption', 'image')
    list_filter = ('subcategory',)

@admin.register(Lieu)
class LieuAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('nom',)}
    list_display = ('nom', 'slug', 'distance_km', 'duree')
    list_filter = ('distance_km',)
    search_fields = ('nom', 'description')

@admin.register(LieuShopping)
class LieuShoppingAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('nom',)}
    list_display = ('nom', 'type', 'region', 'date_ajout')
    search_fields = ('nom', 'description', 'region')
    list_filter = ('type', 'region')



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('title' , 'slug' , 'status' , 'created_on')
    list_filter = ('status',)
    search_fields = ['title', 'content']

@admin.register(MoyenTransport)
class MoyenTransportAdmin(admin.ModelAdmin):
    list_display = ('nom', 'type', 'region', 'site_web', 'telephone')
    prepopulated_fields = {'slug': ('nom',)} # rempli le slug automatiquement
    list_filter = ('type', 'region')
    search_fields = ('nom', 'description', 'region')


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

@admin.register(Sortie)
class SortieAdmin(admin.ModelAdmin):
    list_display = ('nom', 'type')
    prepopulated_fields = {'slug':('nom',)}

@admin.register(ActiviteLoisir)
class ActiviteLoisirAdmin(admin.ModelAdmin):
    list_display = ('nom', 'categorie', 'localisation', 'date_ajout')
    prepopulated_fields = {'slug':('nom',)}
    list_filter = ('categorie',)
    search_fields = ('nom', 'description', 'localisation')
# @admin.register(CarouselSlide)
# class CarouselSlideAdmin(admin.ModelAdmin):
#     list_display = ('title', 'order', 'active')
#     list_editable = ['order', 'active']
######

# admin.site.register(Destinations, DestinationAdmin)
# admin.site.register(PlatTypique)
admin.site.register(APropos)

