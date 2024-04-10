from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Balance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance_euro = models.DecimalField(max_digits=10, decimal_places=2)
    balance_dollar = models.DecimalField(max_digits=10, decimal_places=2)
    balance_inr = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Balance for {self.user.username}"