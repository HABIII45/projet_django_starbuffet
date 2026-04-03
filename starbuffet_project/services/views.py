from django.shortcuts import render,get_object_or_404,redirect
from .models import Traiteur
from .forms import TraiteurFormulaire
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def liste_traiteurs(request):
   les_traiteurs=Traiteur.objects.all()
   context={
        'les_traiteurs':les_traiteurs,
    }
   return render(request,'liste.html',context)
   
def detail_traiteur(request,id):
    le_traiteur=get_object_or_404(Traiteur,id=id)
    traiteur_recuperee={
        'le_traiteur':le_traiteur
    }
    return render(request,'detail_traiteur.html',traiteur_recuperee)

@login_required
def Formulaire(request):
    if request.method == 'POST':
        formulaire=TraiteurFormulaire(request.POST)
        # Vérifier si le formulaire est valide
        if formulaire.is_valid():
           
           # Les données sont valides et nettoyées ! Accès via form.cleaned_data
           nomcomplet = formulaire.cleaned_data['nomcomplet']
           specialite=formulaire.cleaned_data['specialite']
           description=formulaire.cleaned_data['description']
           adresse=formulaire.cleaned_data['adresse']
           est_actif=formulaire.cleaned_data['est_actif']
           email=formulaire.cleaned_data['email']
           
           telephone=formulaire.cleaned_data['telephone']
           image=formulaire.cleaned_data['image']
           try:
               Traiteur.objects.create(
                   nomcomplet = nomcomplet,
                   specialite=specialite,
                   description=description,
                   adresse=adresse,
                   est_actif=est_actif,
                   email=email,
                   
                   telephone=telephone,
                   image=image
                   
               )
               
               messages.success(request,"Votre message a été bien recu merci!")
               return redirect('traiteurs')
           except Exception as e:
               messages.error(request,f"Une erreur s'est produite {e}")
               
    else:
        formulaire=TraiteurFormulaire()
    context={
            'formulaire':formulaire,
            'page_acceuil':"consulter les contacts "
        }
    return render(request,'form_traiteur.html',context)