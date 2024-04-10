from django.shortcuts import render

def home(request):
  return  render (request, 'home.html')

def userdash(request):
  return  render (request, 'user/userdash.html')


def exchange(request):
  return  render (request, 'user/exchangemoney.html')


def send (request):
  return  render (request, 'user/sendmoney.html')


def wire(request):
    return render(request, 'user/wiretransfer.html')


def withdraw (request):
  return  render (request, 'user/withdrawmoney.html')

def paye (request):
  return  render (request, 'user/payementrequest.html')


def deposit (request):
  return  render (request, 'user/depositmoney.html')


