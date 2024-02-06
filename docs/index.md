![logo do projeto](assets/logo.png){ width="300" .center} 

# Notas musicais

Notas musicais é um CLI para ajudar na formação de escalas, acordes e campos harmonicos.

Toda a aplicação é baseada em um comando chamado `notas-musicais`. Esse comando tem um sub-comando relacionado a cada ação que a aplicação pode realizar. Como `escala`, `acorde` e `campo-harmonico`. 

{% include "templates/cards.html" %}

{% include "templates/instalacao.md" %}

## Como usar?

### Escalas

Você pode chamar as escalas via linha de comandos. Por exemplo:

```bash
{{ commands.run }} escala
```

Retornando os graus e as notas correspondentes a essa escala:

```bash
┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━┓
┃ I ┃ II ┃ III ┃ IV ┃ V ┃ VI ┃ VII ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━┩
│ C │ D  │ E   │ F  │ G │ A  │ B   │
└───┴────┴─────┴────┴───┴────┴─────┘
```

#### Alteração de tonica da escala

O primeiro parâmetro do CLI é a tonica da escala que deseja exibir. Desta forma, 
você pode alterar a escala retornada: Por exemplo, a escala de `F#`:

```bash
{{ commands.run }} escala F#
```

Resultando em:

```bash
┏━━━━┳━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ I  ┃ II ┃ III ┃ IV ┃ V  ┃ VI ┃ VII ┃
┡━━━━╇━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ F# │ G# │ A#  │ B  │ C# │ D# │ F   │
└────┴────┴─────┴────┴────┴────┴─────┘
```

#### Alteração ma tonalidade da escala

Você pode alterar a tonalidade da escala também! Esse é o segundo parâmetro da 
linha de comando. Por exemplo, a escala de `D#` menor:

```bash
{{ commands.run }} escala D# menor
┏━━━━┳━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ I  ┃ II ┃ III ┃ IV ┃ V  ┃ VI ┃ VII ┃
┡━━━━╇━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ D# │ F  │ F#  │ G# │ A# │ B  │ C#  │
└────┴────┴─────┴────┴────┴────┴─────┘
```

### Acordes
#### Uso básico
```bash
{{ commands.run }} acorde
┏━━━┳━━━━━┳━━━┓
┃ I ┃ III ┃ V ┃
┡━━━╇━━━━━╇━━━┩
│ C │ E   │ G │
└───┴─────┴───┘
```

#### Variações na cifra
```bash
{{ commands.run }} acorde C+
┏━━━┳━━━━━┳━━━━┓
┃ I ┃ III ┃ V+ ┃
┡━━━╇━━━━━╇━━━━┩
│ C │ E   │ G# │
└───┴─────┴────┘
```

Até ao momento você pode usar acordes maiores, menores, diminutos e aumentados.

## Campo harmonico
Você pode chamar os campos harmonicos via o subcomando `campo-harmonico`. Por exemplo:

```bash
{{ commands.run }} campo-harmonico

┏━━━┳━━━━┳━━━━━┳━━━━┳━━━┳━━━━┳━━━━━━┓
┃ I ┃ ii ┃ iii ┃ IV ┃ V ┃ vi ┃ viiº ┃
┡━━━╇━━━━╇━━━━━╇━━━━╇━━━╇━━━━╇━━━━━━┩
│ C │ Dm │ Em  │ F  │ G │ Am │ Bº   │
└───┴────┴─────┴────┴───┴────┴──────┘

```

Por padrão os parâmetros utilizados são a tônica de `C` e o campo harmonico `maior`

### Alterações nos campos harmonicos

Você pode alterar os parâmetros da tonica e da tonalidade.

```bash
{{ commands.run }} campo-harmonico [TONICA] [TONALIDADE]
```

#### Alteração na tonica do campo

Um exemplo com o campo harmonico de `E`:

```bash
{{ commands.run }} campo-harmonico E
┏━━━┳━━━━━┳━━━━━┳━━━━┳━━━┳━━━━━┳━━━━━━┓
┃ I ┃ ii  ┃ iii ┃ IV ┃ V ┃ vi  ┃ viiº ┃
┡━━━╇━━━━━╇━━━━━╇━━━━╇━━━╇━━━━━╇━━━━━━┩
│ E │ F#m │ G#m │ A  │ B │ C#m │ D#º  │
└───┴─────┴─────┴────┴───┴─────┴──────┘
```

#### Alteração da tonalidade do campo

Um exemplo utilizando o campo harmonico de `E` na tonalidade `menor`:

```bash
{{ commands.run }} campo-harmonico E menor

┏━━━━┳━━━━━┳━━━━━┳━━━━┳━━━━┳━━━━┳━━━━━┓
┃ i  ┃ iiº ┃ III ┃ iv ┃ v  ┃ VI ┃ VII ┃
┡━━━━╇━━━━━╇━━━━━╇━━━━╇━━━━╇━━━━╇━━━━━┩
│ Em │ F#º │ G   │ Am │ Bm │ C  │ D   │
└────┴─────┴─────┴────┴────┴────┴─────┘
```

## Mais informações sobre o CLI

Para descobrir outras opções, você pode usar a flag --help

```bash
{{ commands.run }} --help

Usage: escalas [OPTIONS] [TONICA] [TONALIDADE]                                                       
                                                                                                      
╭─ Commands ─────────────────────────────────────────────────────────────────────────────╮
│ acorde                                                                                 │
│ campo-harmonico                                                                        │
│ escala                                                                                 │
╰────────────────────────────────────────────────────────────────────────────────────────╯
```
### Mais informações sobre os sub-comandos

As informações sobre os sub-comandos podem ser acedidas usando a flag `--help` após 
o nome do parâmetro. Um exemplo do uso do `help` nos campos harmonicos:
```bash
poe {{ commands.run }} campo-harmonico --help
                                                                                          
 Usage: notas-musicais campo-harmonico [OPTIONS] [TONICA] [TONALIDADE]                    
                                                                                          
╭─ Arguments ────────────────────────────────────────────────────────────────────────────╮
│   tonica          [TONICA]      Tonica da escala [default: c]                          │
│   tonalidade      [TONALIDADE]  Tonalidade da escala [default: maior]                  │
╰────────────────────────────────────────────────────────────────────────────────────────╯
╭─ Options ──────────────────────────────────────────────────────────────────────────────╮
│ --help          Show this message and exit.                                            │
╰────────────────────────────────────────────────────────────────────────────────────────╯

```
