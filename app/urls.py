from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import set_language
from django.views.generic import TemplateView

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('articles/', PostAllList.as_view(), name="post_list"),
    path('post/<slug:slug>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<slug:slug>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('culture/', culture_home, name='culture_home'),
    path('culture/<slug:slug>/', category_detail, name='category_detail'),
    path('culture/<slug:category_slug>/<slug:sub_slug>/', subcategory_detail, name='subcategory_detail'),
    path('contact/', contact_view, name='contact'),
    path('a-propos/', a_propos_page, name='a_propos'),
    path('hebergements/', hebergements_list, name='hebergements_list'),
    path('hebergements/<slug:slug>/', hebergement_detail, name='hebergement_detail'),
    path('restaurants/', restaurants_list, name='restaurants_list'),
    path('restaurants/<slug:slug>/', restaurants_detail, name='restaurants_detail'),
    path('infos-pratiques/', infos_pratiques, name='infos_pratiques'),
    path('search/', search, name='search'),
    path('autour_de_babi/', autour_babi, name='autour_de_babi'),
    path('autour_de_babi/<slug:slug>', lieu_autour_babi_detail, name='autour_babi_detail'),
    path('nature/', nature, name='nature'),
    path('nature/<slug:slug>', nature_detail, name='nature_detail'),
    path('sortie/', sortie, name='sortie'),
    path('sortie/<slug:slug>/', sortie_detail, name='sortie_detail'),
    path('loisir/', activites_loisir, name='loisir'),
    path('loisir/<slug:slug>/', activites_loisir_detail, name='loisir_detail'),
    path('shopping/', shopping, name='shopping'),
    path('shopping/<slug:slug>/', shopping_detail, name='shopping_detail'),
    path('transport/', transport, name='transport'),
    path('transport/<slug:slug>/', transport_detail, name='transport'),


    path('mentions-legales/', TemplateView.as_view(template_name="mentions-legales.html"), name="mentions_legales"),
    path('politique-confidentialite/', TemplateView.as_view(template_name="politique-confidentialite.html"), name="politique_confidentialite"),
    path('<slug:slug>/', DetailView.as_view(), name='post_detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
