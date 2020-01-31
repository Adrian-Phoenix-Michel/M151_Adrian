from django.shortcuts import render
from memexicon.models import Memes
from memexicon.forms import MemesForm
from django.views import generic
from PIL import Image
from django.conf import settings


# Create your views here.

def memexicon_submission(request):

    if request.method == "POST":

        form = MemesForm(request.POST, request.FILES)
        if form.is_valid():
            memexicon = form.save(commit=False)
            memexicon.save()
    else:
        form = MemesForm()
    return render(request, 'memexicon_submission.html', {'form': form})


class DiscoveryView(generic.TemplateView):
    template_name = 'memexicon_discovery.html'

    def get_context_data(self, *args, **kwargs):
        memes = super(DiscoveryView, self).get_context_data(**kwargs)
        memes['meme_list'] = Memes.objects.all()
        return memes


def display_memes_images(request):

    if request.method == "GET":

        memes_images = Memes.objects.all()
        return render(request, 'memexicon_discovery.html', {
            'memes_images': memes_images,
            'static_url': settings.STATIC_URL
        })

#    model = Memes

#    def get_context_data(self, **kwargs):
#        memes = super(DiscoveryView, self).get_context_data(**kwargs)
#        memes['meme_list'] = Memes.objects.all()
#        return render(self, 'memexicon_discovery.html')


#    def get_queryset(self):
#        return Memes.objects.all()
