from django import forms

class TraiteurFormulaire(forms.Form):
    nomcomplet=forms.CharField(
        label="nom complet",
        max_length=100,
        widget=forms.TextInput(attrs={'placholder' :"Votre nom complet"})
        
    )
    specialite=forms.CharField(
        label="specialité",
        max_length=100,
        widget=forms.TextInput(attrs={'placholder' :"Votre specialité"})
        
    )
    description=forms.CharField(
        label="description",
        max_length=100,
        widget=forms.TextInput(attrs={'placholder' :"donner une petite description"})
        
        
    )
    adresse=forms.CharField(
        label="adresse",
        max_length=100,
        widget=forms.TextInput(attrs={'placholder' :"votre adresse"})
        
        
    )
    est_actif=forms.BooleanField(
        label="statut",
        #widget=forms.TextInput(attrs={'placholder' :"donner le statut"})
        
    )
    email=forms.EmailField(
        label="email",
        max_length=100,
        widget=forms.TextInput(attrs={'placholder' :"Votre mail exemple@gmail.com"})
        
    )
    telephone=forms.CharField(
        label="tel",
        max_length=100,
        widget=forms.TextInput(attrs={'placholder' :"Votre numero de tel"})
        
    )
    description=forms.CharField(
        label="description",
        max_length=100,
        widget=forms.TextInput(attrs={'placholder' :"donner une petite description"})
        
    )
    image=forms.URLField(
        label="image",
        max_length=100,
        widget=forms.TextInput(attrs={'placholder' :"donner une image"})
        
    )