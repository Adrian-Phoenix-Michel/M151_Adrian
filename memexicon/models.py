from django.db import models


# Create your models here.

class Memes(models.Model):
    meme_img = models.ImageField(upload_to='static/')
    meme_name = models.CharField(max_length=50)
    popularity = models.IntegerField()


class MemesInDetail(models.Model):
    meme_id = models.ForeignKey(Memes, on_delete=models.CASCADE)
    origin = models.CharField(max_length=1000)
