from typing import List

from pypro.modulos.models import Modulo, Aula

"""
   Lista módulos ordenados por títulos
   :return:
   """


def listar_modulos_ordenados() -> List[Modulo]:

    return list(Modulo.objects.order_by('order').all())


def encontrar_modulo(slug: str) -> Modulo:
    return Modulo.objects.get(slug=slug)


def listar_aula_de_modulo_ordenadas(modulo: Modulo):
    return list(modulo.aula_set.order_by('order').all())


def encontrar_aula(slug):
    return Aula.objects.select_related('modulo').get(slug=slug)
