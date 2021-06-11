from django.shortcuts import render
#from django.contrib.auth.decorators import login_required
from pypro.modulos import facade


def indice(request):
    ctx = {'modulo': facade.listar_modulo_com_aula()}
    return render(request, 'modulos/indice.html', ctx)


def detalhe(request, slug):
    modulo = facade.encontrar_modulo(slug)
    aulas = facade.listar_aulas_de_modulos_ordenados(modulo)
    return render(request, 'modulos/modulo_detalhe.html', {'modulo': modulo, 'aulas': aulas})
