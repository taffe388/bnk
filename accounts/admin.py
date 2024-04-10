from django.contrib import admin
from .models import Accounts
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from django.contrib import admin
from .models import Accounts
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class AccountAdmin(UserAdmin):
    
    list_display = ('email', 'nom', 'prenom', 'username', 'last_login', 'date_joined', 'is_active') # Affiche les colonnes dans la liste des utilisateurs dans le panneau d'administration
    
    list_display_links = ('email', 'nom', 'prenom')  # Ajoute des liens cliquables pour accéder aux détails de l'utilisateur à partir de ces colonnes
    
    readonly_fields = ('last_login', 'date_joined')  # Rend les champs 'last_login' et 'date_joined' en lecture seule
    
    ordering = ('-date_joined',) # Détermine l'ordre de tri par défaut de la liste des utilisateurs
    
    filter_horizontal = ()  # Permet la sélection d'autres objets dans un champ ManyToMany (non utilisé dans cet exemple)
   
    list_filter = ()  # Ajoute des filtres de recherche dans le panneau d'administration
    
    # Définit des groupes de champs pour la gestion des utilisateurs dans le panneau d'administration
    fieldsets = () 

    

admin.site.register(Accounts, AccountAdmin)
