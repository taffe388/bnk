"""
URL configuration for banques project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include 
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home, name='home'),

    path('accounts/', include('accounts.urls')),

    path ('user/userdash/', views.userdash , name= 'userdash' ),

    path ('user/exchangemoney/', views.exchange , name= 'exchange' ),

    path ('user/sendmoney/', views.send , name= 'send' ),

    path ('user/wiretransfer/', views.wire , name= 'wire' ),

    path ('user/withdraw/', views.withdraw , name= 'withdraw' ),

    path ('user/payementrequest/', views.paye , name= 'paye' ),

      path ('user/depositmoney/', views.deposit , name= 'deposit' ),

    

    

]
