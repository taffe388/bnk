from base64 import urlsafe_b64decode
from email import message
from django.contrib import messages, auth
from django.shortcuts import redirect, render
from .models import Accounts
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            prenom = form.cleaned_data['prenom']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split('@')[0]
            user = Accounts.objects.create_user(nom=nom, prenom=prenom, email=email, username=username, password=password)
            user.phone_number = phone_number
            user.save()

            #Activation de l'utilisateur 
            current_site=get_current_site(request)
            mail_subject= ' Conferma della creazione del conto e elaborazione della tua richiesta'
           
            message = render_to_string('accounts/accounts_verification_email.html', {
                'user': user,
                'domaine': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })

            to_email=email
            send_email= EmailMessage(mail_subject , message , to=[to_email])
            send_email.send()


            #messages.success(request, 'Enregistrement réussi')
            return redirect('/accounts/login/?command=verification&email='+ email)
    else:
        form = RegistrationForm()

    context = {
        'form': form 
    }
         
    return render(request, 'accounts/register.html', context)

def login(request):
    if request.method == 'POST':
        email_address = request.POST.get('email')
        password = request.POST.get('password')
        
        user = auth.authenticate(email=email_address, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('userdash')
        else:
            messages.error(request, 'Accesso non valido')
            return redirect('login')

    return render(request, 'accounts/login.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'Siete disconnessi')
    return redirect('login')




def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = user.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, user.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Congratulazioni, il vostro account è stato attivato.')
        return redirect('login')
    else:
        messages.error(request, 'Il link di attivazione non è valido. Si prega di riprovare.')
        return redirect('register')


