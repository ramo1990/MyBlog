from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
# from .views import create_post

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('post/<slug:slug>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<slug:slug>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('destinations/', DestinationListView.as_view(), name='destination_list'),
    path('destinations/<slug:slug>/', DestinationDetailView.as_view(), name='destination_detail'),
    path('<slug:slug>/', DetailView.as_view(), name='post_detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
