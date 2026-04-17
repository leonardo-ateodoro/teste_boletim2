import pytest
from boletim.calculos import calcular_media     

def test_lista_vazia():
    with pytest.raises(ValueError, match="A lista de notas não pode estar vazia."):
        calcular_media([])

def test_string_como_lista():
    with pytest.raises(TypeError, match="As notas devem ser uma lista numérica"):
        calcular_media("OITO")

def test_notas_nao_numericas():
    with pytest.raises(TypeError, match="As notas devem ser uma lista numérica"):
        calcular_media(["um", "oito"])

def test_notas_numericas_e_nao_numericas():
    with pytest.raises(TypeError, match="As notas devem ser uma lista numérica"):
        calcular_media([10, "cinco", 4])

def test_numeros_maiores_que_10():
    with pytest.raises(ValueError, match="As notas devem estar entre 0 e 10."):
        calcular_media([11, 100])

def test_numeros_menores_0():
    with pytest.raises(ValueError, match="As notas devem estar entre 0 e 10."):
        calcular_media([-1, 5, 7])

