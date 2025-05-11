from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import create_post

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('new/', create_post, name='create_post'), # URL pour créer un post
    path('<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('<slug:slug>/edit/', views.update_post, name='update_post')
    
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
