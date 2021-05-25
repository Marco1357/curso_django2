from typing import List

from pypro.modulos.models import Modulo

"""
   Lista módulos ordenados por títulos
   :return:
   """


def listar_modulos_ordenados() -> List[Modulo]:
    return list(Modulo.objects.order_by('order').all())


def encontrar_modulo(slug: str) -> Modulo:
    return Modulo.objects.get(slug=slug)
