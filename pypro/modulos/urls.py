from pypro.modulos import views
from pypro.urls import path


app_name = 'modulos'
urlpatterns = [
    path('<slug:slug>', views.detalhe, name='detalhe'),
    path('aulas/<slug:slug>', views.aula, name='aula'),
    path('', views.indice, name='indice'),
]
