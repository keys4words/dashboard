from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h2>Home accounts')

def products(request):
    return HttpResponse('<h2>Products accounts')

def customers(request):
    return HttpResponse('<h2>customers accounts')