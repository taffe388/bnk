from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
    def create_user(self, nom, prenom, email, username, password=None):
        if not email:
            raise ValueError('Veuillez définir votre email')
        if not username:
            raise ValueError('Veuillez définir votre nom utilisateur')
        
        # Crée une nouvelle instance du modèle utilisateur avec les données fournies.
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            nom=nom,
            prenom=prenom,
        )
        # Définit le mot de passe pour l'utilisateur.
        user.set_password(password)
        # Sauvegarde l'utilisateur dans la base de données.
        user.save(using=self._db)
        return user

    def create_superuser(self, nom, prenom, email, username , password):
      
        # Utilise la méthode create_user pour créer un utilisateur avec les paramètres fournis.
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            nom=nom,
            prenom=prenom,
        )
        # Définit les attributs spécifiques au superutilisateur.
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        # Sauvegarde l'utilisateur dans la base de données.
        user.save(using=self._db)
        return user


class Accounts(AbstractBaseUser):
    """
    Modèle utilisateur personnalisé pour gérer les comptes utilisateurs.
    """
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=50)  # Valeur par défaut ''

    # Attributs requis
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    # Attributs spécifiques pour la gestion des utilisateurs
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'nom', 'prenom']

    # Lien vers le gestionnaire personnalisé
    objects = MyAccountManager()

    def __str__(self):   # Méthode renvoyant une représentation sous forme de chaîne de l'objet.  str: Adresse email de l'utilisateur.
       
        return self.email

    def has_perm(self, perm, obj=None):  #Méthode renvoyant True si l'utilisateur a la permission spécifiée.  perm (str): Permission à vérifier. obj (object): Objet sur lequel vérifier la permission (non utilisé ici).

        return self.is_admin

    def has_module_perms(self, add_module): #  Méthode renvoyant True si l'utilisateur a des permissions sur le module spécifié.  add_module (str): Module pour lequel vérifier les permissions (non utilisé ici).
        return True