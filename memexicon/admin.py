from django.contrib import admin
from memexicon.models import Memes


# Register your models here.

class MemesAdmin(admin.ModelAdmin):
    list_display = ('meme_img', 'meme_name', 'popularity')
    search_fields = ('meme_img', 'meme_name', 'popularity')


admin.site.register(Memes, MemesAdmin)


