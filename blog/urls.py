from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import set_language

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),  # nécessaire pour le changement de langue
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
)
urlpatterns += [
    path('i18n/setlang/', set_language, name='set_language'),
]
# Pour les fichiers médias en dev
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)