from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import set_language
from django.views.generic import TemplateView

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path("articles/", PostAllList.as_view(), name="post_list"),
    path('post/<slug:slug>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<slug:slug>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('destinations/', DestinationListView.as_view(), name='destination_list'),
    path('destinations/<slug:slug>/', DestinationDetailView.as_view(), name='destination_detail'),
    path('culture/', CultureListView.as_view(), name='culture'),
    path('culture/<slug:slug>/', CultureDetailView.as_view(), name='culture_detail'),
    path('agenda/', agenda_list, name='agenda_list'),
    path('agenda/<slug:slug>/', agenda_detail, name='agenda_detail'),
    path('gastronomie/', gastronomie_list, name='gastronomie_list'),
    path('gastronomie/<slug:slug>/', gastronomie_detail, name='gastronomie_detail'),
    path('ville/', ville_list, name='ville_list'),
    path('ville/<slug:slug>/', ville_detail, name='ville_detail'),
    path('conseils/', conseils_view, name='conseils'),
    path('contact/', contact_view, name='contact'),
    path('a-propos/', a_propos_page, name='a_propos'),
    path('hebergements/', hebergements_list, name='hebergements_list'),
    path('hebergements/<slug:slug>/', hebergement_detail, name='hebergement_detail'),
    path('restaurants/', restaurants_list, name='restaurants_list'),
    path('restaurants/<slug:slug>/', restaurants_detail, name='restaurants_detail'),
    path('infos-pratiques/', infos_pratiques, name='infos_pratiques'),
    path('que_faire/', que_faire, name='que_faire'),
    path('que_faire/<slug:slug>/', detail_activite, name='detail_activite'),
    path('search/', search, name='search'),
    path('mentions-legales/', TemplateView.as_view(template_name="mentions-legales.html"), name="mentions_legales"),
    path('politique-confidentialite/', TemplateView.as_view(template_name="politique-confidentialite.html"), name="politique_confidentialite"),
    # path('favori/<int:restaurant_id>/', toggle_favorite, name='toggle_favorite'),
    # path('mes-favoris/', mes_favoris, name='mes_favoris'),
    path('<slug:slug>/', DetailView.as_view(), name='post_detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
