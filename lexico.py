import ply.lex as lex  # inportaçao da biblioteca


def lexico(t, erro):
    saidas.append((t.lineno, t.lexpos, t.type, t.value, erro))

    # palavras reservadas

    resersed = {
        'IFSULDEMINAS': 'IFSULDEMINAS',
        'INICIO': 'INICIO',
        'COMPILADORES': 'COMPILADORES',
        'FIM': 'FIM',
        'LER': 'LER',
        'IMPRIMIR': 'IMPRIMIR',
        'RETORNA': 'RETORNA',
        'SE': 'SE',
        'SENAO': 'SENAO',
        'SENAO_SE': 'SENAO_SE',
        'PARA': 'PARA',
        'ENQUANTO': 'ENQUANTO',
        'FACA': 'FACA',
        'FUNCAO': 'FUNCAO',
        'CASO_FOR': 'CASO_FOR',
        'SAIR': 'SAIR'
    }

    tokens = [


        'mais',  # +
        'menos',  # -
        'vezes',  # *
        'dividir',  # /
        'modulo',  # %


        'dois_pontos',
        'ponto_virgula',
        'virgula',
        'ponto',
        'aspas'
        'aspas_simples'
        'comentario_uma_linha'
        'comentario_n_linha'


        'negacao',
        'igual',
        'mais_igual',
        'menos_igual',
        'vezes_igual',
        'divide_igual',



        'menor',
        'maior',
        'menor_igual',
        'maior_igual',
        'exatamente_igual',
        'diferente',
        'e',
        'ou',


        'abre_parentese',
        'fecha_parentese',
        'abre_cochete',
        'fecha_colchete',
        'abre_chave',
        'fecha_chave',

        'inteiro',
        'flutuante',
        'texto',
        'variavel',
        'numero',

        'ignore',

        'variavel_errado',
        'numero_errado',
        'texto_errrado'



    ] + list(reversed.values())

    # expressoes regulares dos tokens simples

    # matematicos
    t_mais = r'\+'
    t_menos = r'-'
    t_vezes = r'\*'
    t_dividir = r'/'
    t_modulo = r'%'

    # pontos

    t_dois_pontos = r'\:'
    t_ponto_virgula = r'\;'
    t_virgula = r'\,'
    t_ponto = r'\.'
    t_aspas = r'\"'
    t_aspas_simples = r'\''

    t_negacao = r'\~'
    t_igual = r'\='
    t_mais_igual = r'\+\='
    t_menos_igual = r'\-\='
    t_vezes_igual = r'\*\='
    t_divide_igual = r'\/\='

    t_menor = r'\<'
    t_maior = r'\>'
    t_menor_igual = r'\<\='
    t_maior_igual = r'\>\='
    t_duplo_igual = r'\=\='
    t_diferente = r'\!\='
    t_e = r'\&'
    t_ou = r'\|'

    # escopo

    t_abre_parentese = r'\('
    t_fecha_parentese = r'\)'
    t_abre_colchete = r'\['
    t_fecha_colchete = r'\]'
    t_abre_chave = r'\{'
    t_fecha_chave = r'\}'

    # comentario

    t_comentario_uma_linha = r'#.*$'
    t_comentario_n_linha = r'#\*(.|\n)*?\*#'

    # expressoes regulares dos tokens complexos

    def t_variavel(self, t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        # verificando se sera, palavra reservada .
        if t.value in resersed:

            t.type = resersed[t.value]
            return lexico(t, f"Palavra Reservada")

        else:
            return lexico(t, f"Correto")

    def t_variavel_errado(t):
        r'([0-9]+[a-z]+)|([@!#$%&*]+[a-z]+|[a-z]+\.[0-9]+|[a-z]+[@!#$%&*]+)'
        return lexico(t, f"veriavel com erro")

    def t_numero(self, t):
        r'-?\d+(\.\d+)?'
        return lexico(t, f"Correto")

    def t_numero_errado(self, t):
        r'([0-9]+\.[a-z]+[0-9]+)|([0-9]+\.[a-z]+)|([0-9]+\.[0-9]+[a-z]+)'
        return lexico(t, f"Numero com erro ")

    def t_texto(t):
        r'"[^(|\n)]*"'
        return lexico(t, f"Correto")

    def t_texto_errado(self, t):
        r'("[^"]*)'
        return lexico(t, f"string (texto) com erro ")

    def t_flutuante(t):
        r'([0-9]+\.[0-9]+)|([0-9]+\.[0-9]+)'
        t.value = float(t.value)
        return lexico(t, f"Correto")

    def t_inteiro(t):
        r'\d+'
        t.value = int(t.value)
        return t

    def t_nova_linha(t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    def t_erro(t):
        return saidas.append((t.lineno, t.lexpos, f'invalido', t.value, f'Caracter não faz parte da linguagem'))
