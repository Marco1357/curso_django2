from django.http import HttpResponse
from django,schortcuts import render

# Create your views here.


def home(request):
    return HttpResponse('Olá Django')
