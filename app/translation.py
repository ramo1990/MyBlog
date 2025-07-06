from modeltranslation.translator import register, TranslationOptions
from .models import *

@register(Hebergement)
class HebergementTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'adresse','services', 'accessibility', 'conseil')  # les champs que tu veux traduire

@register(Restaurant)
class RestaurantTranslationOptions(TranslationOptions):
    fields = ('title', 'content', 'adresse', 'specialite', 'conseil')

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(SubCategory)
class SubCategoryTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'services', 'accessibility', 'conseil', 'activite', 'horaire', 'adresse',)

@register(GalleryImage)
class GalleryImageTranslationOptions(TranslationOptions):
    fields = ('caption',)

@register(LieuShopping)
class LieuShoppingTranslationOptions(TranslationOptions):
    fields = ('nom', 'description', 'adresse', 'region', 'services', 'accessibility', 'conseil',)

@register(Lieu)
class LieuTranslationOptions(TranslationOptions):
    fields = ('nom', 'description', 'adresse', 'services', 'accessibility', 'conseil')

@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)

@register(ActiviteLoisir)
class ActiviteLoisirTranslationOptions(TranslationOptions):
    fields = ('nom', 'description', 'activite_proposee', 'accessibilite')

@register(Sortie)
class SortieTranslationOptions(TranslationOptions):
    fields = ('nom', 'description', 'acces', 'programme', 'dress_code')

# @register(Restaurant)
# class RestaurantTranslationOptions(TranslationOptions):
#     fields = ('title', 'content', 'specialite', 'conseil')

@register(MoyenTransport)
class MoyenTransportTranslationOptions(TranslationOptions):
    fields = ('nom', 'description', 'horaires', 'tarifs', 'conseil', 'zone_desservi', 'services')

@register(APropos)
class AProposTranslationOptions(TranslationOptions):
    fields = ('title', 'content')

@register(InfoPratique)
class InfoPratiqueTranslationOptions(TranslationOptions):
    fields = ('title', 'content')