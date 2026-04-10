from boletim.calculos import calcular_media
import pytest

@pytest.mark.parametrize("notas, esperado",
                         [
                             ([10,5,3], 6.0),
                              ([5.5,6.3,8.2], 6.7),
                              ([5.5,7,8], 6.8),
                              ([1,10,8,5.5,3,7,6.7,7.6,3 ], 5,9),
                              ([0,0,0], 0),
                              ([10,10,10],10)
                         ])
def test_boletim_happy_patch(notas, esperado):
    assert calcular_media (notas) == esperado