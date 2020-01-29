from django.db import models


# Create your models here.

class Memes(models.Model):
    meme_img = models.ImageField()
    meme_name = models.CharField(max_length=50)
    popularity = models.IntegerField()


class MemesInDetail(models.Model):
    meme_id = models.ForeignKey(Memes, on_delete=models.CASCADE)
    img_fk = models.ForeignKey(Memes.meme_img, on_delete=models.CASCADE)
    name_fk = models.ForeignKey(Memes.meme_name, on_delete=models.CASCADE)
    popularity_fk = models.ForeignKey(Memes.popularity, on_delete=models.CASCADE)
    origin = models.CharField(max_length=1000)
