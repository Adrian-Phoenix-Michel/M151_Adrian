from django.shortcuts import render
from memexicon.forms import MemesForm


# Create your views here.

def memexicon_view(request):
    if request.method == "POST":
        form = MemesForm(request.POST)
        if form.is_valid():
            memexicon = form.save(commit=False)
            memexicon.save()
    else:
        form = MemesForm()
    return render(request, 'memexicon.html', {'form': form})
