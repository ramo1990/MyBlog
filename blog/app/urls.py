from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *
# from .views import create_post

urlpatterns = [
    path('', PostList.as_view(), name='home'),
    # path('new/', create_post, name='create_post'), # URL pour créer un post
    path('<slug:slug>/', DetailView.as_view(), name='post_detail'),
    path('post/<slug:slug>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('post/<slug:slug>/delete/', PostDeleteView.as_view(), name='post_delete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
