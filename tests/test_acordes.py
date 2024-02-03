from pytest import mark

from notas_musicais.acordes import acorde

"""
Entrada
acorde Cm

Esperado:
I - III - V
C    E    G

{'notas': ['C', 'E', 'G'], 'graus': ['I', 'III', 'V']}
"""


@mark.parametrize(
    'nota,esperado',
    [
        ('C', ['C', 'E', 'G']),
        ('Cm', ['C', 'D#', 'G']),
        ('Cº', ['C', 'D#', 'F#']),
        ('C+', ['C', 'E', 'G#']),
        ('Cm+', ['C', 'D#', 'G#']),
        ('F#', ['F#', 'A#', 'C#']),
    ],
)
def teste_acorde_deve_retornar_as_notas_correspondentes(nota, esperado):
    (notas, graus) = acorde(nota).values()

    assert esperado == notas


@mark.parametrize(
    'cifra,esperado',
    [
        ('C', ['I', 'III', 'V']),
        ('Cm', ['I', 'III-', 'V']),
        ('Cº', ['I', 'III-', 'V-']),
        ('C+', ['I', 'III', 'V+']),
        ('Cm+', ['I', 'III-', 'V+']),
    ],
)
def teste_acorde_deve_retornar_as_graus_correspondentes(cifra, esperado):
    (notas, graus) = acorde(cifra).values()

    assert esperado == graus
