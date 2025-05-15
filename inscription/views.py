from django.shortcuts import render
from .forms import CandidatForm

# Vue d'inscription
def inscrire(request):
    if request.method == 'POST':
        form = CandidatForm(request.POST, request.FILES)
        if form.is_valid():
            candidat = form.save()
            return render(request, 'inscription/recu.html', {'candidat': candidat})
    else:
        form = CandidatForm()
    return render(request, 'inscription/formulaire.html', {'form': form})

# Vue pour la page d'accueil (ajoutée pour corriger l'erreur)
def home(request):
    return render(request, 'inscription/home.html')  # Crée le template 'home.html' dans le dossier templates
