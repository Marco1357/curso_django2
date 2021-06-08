import pytest
from django.urls import reverse
from model_mommy import mommy
from pypro.django_assertions import assert_contains
from pypro.modulos.models import Modulo, Aula


@pytest.fixture
def modulo(db):
    return mommy.make(Modulo)


@pytest.fixture
def aula(modulo):
    return mommy.make(Aula, modulo=modulo)


@pytest.fixture
def resp(client, aula):
    resp = client.get(reverse('modulos:aula', kwargs={'slug': aula.slug}))
    return resp


def test_titulos(resp, aula: Aula):
    assert_contains(resp, aula.titulo)


def test_yuotube(resp, aula: Aula):
    assert_contains(resp, f'src="https://www.youtube.com/embed/{ aula.youtube_id }"')


def test_modulo_breadcrumb(resp, modulo: Modulo):
    assert_contains(resp, f'<li class="breadcrumb-item"><a href="{modulo.get_absolute_url()}')


def test_modulo_url(resp, modulo: Modulo):
    assert_contains(resp, modulo.get_absolute_url())
