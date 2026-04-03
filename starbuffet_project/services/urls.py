from django.urls import path
from .views import liste_traiteurs
from .views import detail_traiteur
from .views import Formulaire

urlpatterns = [
    path('liste_traiteurs/',liste_traiteurs,name='traiteurs'),
    path('liste_traiteurs/<int:id>/',detail_traiteur,name='details'),
    path('ajouter/',Formulaire,name='ajouter_traiteur'),
]