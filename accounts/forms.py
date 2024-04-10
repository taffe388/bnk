# forms.py
from django import forms
from .models import Accounts

class RegistrationForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Mot de Passe'
    }))

    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirmez Mot de passe '
    }))


    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError(
            "le mot de passe ne correspond pas" 
            )

    class Meta:
        model = Accounts
        fields = ['nom', 'prenom', 'phone_number', 'email', 'password']


    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)

        self.fields['nom'].widget.attrs['placeholder']='Entrer votre nom'
        self.fields['prenom'].widget.attrs['placeholder']='Entrer votre prenom'
        self.fields['phone_number'].widget.attrs['placeholder']='Entrer votre numeros '
        self.fields['email'].widget.attrs['placeholder']='Entrer votre email'


        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'