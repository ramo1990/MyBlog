from django.contrib import admin
from .models import *

# @admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title' , 'slug' , 'status' , 'created_on')
    list_filter = ('status',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}  # <- auto-remplit le champ slug côté admin

    class Media:
        js = ('admin/js/jquery.init.js',) # pour forcer l'init jQuery dans admin


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

admin.site.register(Post , PostAdmin)
admin.site.register(Destinations, DestinationAdmin)
# admin.site.register(Culture)
admin.site.register(ConseilVoyage)
admin.site.register(MessageContact)
admin.site.register(APropos)
# Register your models here.

