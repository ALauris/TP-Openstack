from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.http import Http404

from django.shortcuts import render, get_object_or_404
from .forms import FichierForm
from fichier.models import Fichier

def ajouter_fichier(request):
    sauvegarde = False
    form = FichierForm(request.POST or None, request.FILES)
    if form.is_valid():
        fichier = Fichier()
        fichier.description = form.cleaned_data["description"]
        fichier.fichier = form.cleaned_data["fichier"]
        fichier.save()
        sauvegarde = True

    return render(request, 'fichier/ajouter_fichier.html', {
        'form': form, 
        'sauvegarde': sauvegarde
    })
	
def voir_fichiers(request):
    return render(
        request, 
        'fichier/voir_fichiers.html', 
        {'fichiers': Fichier.objects.all()}
    )