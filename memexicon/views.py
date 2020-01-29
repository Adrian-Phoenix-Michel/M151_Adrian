from django.shortcuts import render
from memexicon.forms import MemesForm


# Create your views here.

def memexicon_submission(request):
    if request.method == "POST":
        form = MemesForm(request.POST, request.FILES)
        if form.is_valid():
            memexicon = form.save(commit=False)
            memexicon.save()
            return render(request, 'memexicon.html', {'form': form})
        else:
            error = form.errors
            return render(request, 'memexicon.html', {
                'form': form,
                'alert': error
            })
    else:
        form = MemesForm()
        return render(request, 'memexicon.html', {'form': form})

