from notas_musicais.escalas import ESCALAS, NOTAS, escala


def triade(nota, tonalidade):
    graus = (0, 2, 4)
    notas_da_escala, g = escala(nota, tonalidade).values()

    return [notas_da_escala[grau] for grau in graus]


def _menor(cifra):
    nota, g = cifra.split('m')
    if '+' in cifra:
        tonica, terca, quinta = triade(nota, 'menor')
        notas = [tonica, terca, semitom(quinta, intervalo=+1)]
        graus = ['I', 'III-', 'V+']
    else:
        notas = triade(nota, 'menor')
        graus = ['I', 'III-', 'V']

    return notas, graus


def semitom(nota, *, intervalo):
    pos = NOTAS.index(nota) + intervalo

    return NOTAS[pos % 12]


def acorde(cifra: str) -> dict[str, list[str]]:
    """
    Gera as notas de um acorde partindo de uma cifra.

    Parameters:
        cifra: Um acorde em forma de cifra

    Returns:
        Um dicionário com as notas e graus correspondentes à escala maior

    Examples:
        >>> acorde('C')
        {'notas': ['C', 'E', 'G'], 'graus': ['I', 'III', 'V']}

        >>> acorde('Cm')
        {'notas': ['C', 'D#', 'G'], 'graus': ['I', 'III-', 'V']}

        >>> acorde('Cº')
        {'notas': ['C', 'D#', 'F#'], 'graus': ['I', 'III-', 'V-']}

        >>> acorde('C+')
        {'notas': ['C', 'E', 'G#'], 'graus': ['I', 'III', 'V+']}

        >>> acorde('Cm+')
        {'notas': ['C', 'D#', 'G#'], 'graus': ['I', 'III-', 'V+']}
    """

    if 'm' in cifra:
        notas, graus = _menor(cifra)
    elif 'º' in cifra:
        (nota, g) = cifra.split('º')
        tonica, terca, quinta = triade(nota, 'menor')
        notas = [tonica, terca, semitom(quinta, intervalo=-1)]
        graus = ['I', 'III-', 'V-']
    elif '+' in cifra:
        nota, g = cifra.split('+')
        tonica, terca, quinta = triade(nota, 'maior')
        notas = [tonica, terca, semitom(quinta, intervalo=+1)]
        graus = ['I', 'III', 'V+']
    else:
        notas = triade(cifra, 'maior')
        graus = ['I', 'III', 'V']

    return {'notas': notas, 'graus': graus}
