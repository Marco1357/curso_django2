from pypro.turmas import views
from pypro.urls import path


app_name = 'turmas'
urlpatterns = [
    path('', views.indice, name='indice'),
]
