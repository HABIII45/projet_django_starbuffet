from django.contrib import admin
from .models import Traiteur
# Register your models here.
class AjoutTraiteur(admin.ModelAdmin):
    list_display=('nomcomplet','specialite','description','adresse','est_actif','email','date_creation','telephone','image')

    list_filter=('specialite','date_creation')
    search_fields=('nomcomplet','specialite')
    
admin.site.register(Traiteur,AjoutTraiteur)