from django.contrib import admin
from django.urls import path
from . import views

app_name = 'memexicon'
urlpatterns = [
    path('', views.memexicon_submission, name='memexicon_submission')
]