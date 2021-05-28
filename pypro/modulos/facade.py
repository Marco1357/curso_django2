from typing import List

from pypro.modulos.models import Modulo

"""
   Lista módulos ordenados por títulos
   :return:
   """


def listar_modulos_ordenados() -> List[Modulo]:
    """

    :rtype: object
    """
    return list(Modulo.objects.order_by('order').all())


def encontrar_modulo(slug: str) -> Modulo:
    return Modulo.objects.get(slug=slug)


def listar_modulos_ordenadas(modulo: Modulo):
    return list(modulo.aula_set.order_by('order').all())
