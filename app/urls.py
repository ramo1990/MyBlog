from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import set_language

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('post/<slug:slug>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<slug:slug>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('destinations/', DestinationListView.as_view(), name='destination_list'),
    path('destinations/<slug:slug>/', DestinationDetailView.as_view(), name='destination_detail'),

    path('culture/', CultureListView.as_view(), name='culture'),
    path('culture/<slug:slug>/', CultureDetailView.as_view(), name='culture_detail'),

    path('conseils/', conseils_view, name='conseils'),
    path('contact/', contact_view, name='contact'),
    path('a-propos/', a_propos_page, name='a_propos'),
    path('i18n/setlang/', set_language, name='set_language'),  # ✅ permet à reverse('set_language') de fonctionner
    path('<slug:slug>/', DetailView.as_view(), name='post_detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
