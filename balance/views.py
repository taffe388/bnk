from django.shortcuts import render
from .models import Balance

def my_view(request):
    # Obtenez l'utilisateur actuellement connecté
    user = request.user

    # Obtenez la balance de l'utilisateur actuel
    try:
        balance = Balance.objects.get(user=user)
    except Balance.DoesNotExist:
        # Créez une nouvelle instance de Balance avec les soldes à zéro
        balance = Balance.objects.create(
            user=user,
            balance_euro=0,
            balance_dollar=0,
            balance_inr=0
        )

    # Passer la balance au modèle de template
    return render(request, 'user/userdash.html', {'balance': balance})
