import pytest
from licitações import avaliar_proposta

def test_aprovado():
    assert avaliar_proposta([8, 7, 9]) == "Aprovado"

def test_reprovado():
    assert avaliar_proposta([5, 6, 4]) == "Reprovado"

def test_lista_vazia():
    with pytest.raises(ValueError):
        avaliar_proposta([])

def test_media_limite():
    assert avaliar_proposta([7, 7, 7]) == "Aprovado"
    assert avaliar_proposta([6.9, 7, 7]) == "Reprovado"
