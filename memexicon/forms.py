from django import forms
from memexicon.models import Memes


class MemesForm(forms.ModelForm):
    class Meta:
        model = Memes
        fields = ('meme_img', 'meme_name', 'popularity')
