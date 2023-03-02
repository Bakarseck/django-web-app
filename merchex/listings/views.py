from django.shortcuts import render
from django.shortcuts import HttpResponse

def hello(request):
    return HttpResponse('<h1>Hello Django!</h1>')

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')

def listings(request):
    return HttpResponse('<h1>Listings</h1>')

def contact(request):
    return HttpResponse('<h1>Contact Us</h1>')
