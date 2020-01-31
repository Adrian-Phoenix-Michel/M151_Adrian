from django.contrib import admin
from django.urls import path
from . import views
from .views import DiscoveryView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'memexicon'
urlpatterns = [
    path('submit/', views.memexicon_submission, name='memexicon_submission'),
    path('discovery/', DiscoveryView.as_view(), name='discovery'),
    path('memes_images/', views.display_memes_images, name='memes_images')
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
