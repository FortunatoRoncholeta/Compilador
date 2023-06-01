import ply.lex as lex  # inportaçao da biblioteca

saidas = []


def lexico(t, erro):
    saidas.append((t.lineno, t.lexpos, t.type, t.value, erro))


# palavras reservadas
reserved = {
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
    'SAIR': 'SAIR',
    'FUNCAO': 'FUNCAO',
    'TINTEIRO': 'TINTEIRO',
    'FLUTUANTE': 'FLUTUANTE',
    'TEXTO': 'TEXTO'
}

tokens = [
    'OPmath',  # +


    'dois_pontos',
    'ponto_virgula',
    'virgula',
    'ponto',
    'aspas',
    'aspas_simples',
    'comentario_uma_linha',
    # 'comentario_n_linha',


    'negacao',
    'OPatr',


    'OPcomp',

    'OPlog',



    'abre_parentese',
    'fecha_parentese',
    'abre_colchete',
    'fecha_colchete',
    'abre_chave',
    'fecha_chave',

    'inteiro',
    'flutuante',
    'texto',
    'variavel',

    'ignore',

    'variavel_errada',
    'numero_errado',
    'texto_errado',
    'caracter_invisivel'



] + list(reserved.values())

t_IFSULDEMINAS = r'IFSULDEMINAS'
t_INICIO = r'INICIO'
t_COMPILADORES = r'COMPILADORES'
t_FIM = r'FIM'
t_LER = r'LER'
t_IMPRIMIR = r'IMPRIMIR'
t_RETORNA = r'RETORNA'
t_SE = r'SE'
t_SENAO = r'SENAO'
t_SENAO_SE = r'SENAO_SE'
t_PARA = r'PARA'
t_ENQUANTO = r'ENQUANTO'
t_FACA = r'FACA'
t_FUNCAO = r'FUNCAO'
t_CASO_FOR = r'CASO_FOR'
t_SAIR = r'SAIR'
t_TINTEIRO = r'INTEIRO'
t_FLUTUANTE = r'FLUTUANTE'
t_TEXTO = r'TEXTO'

# matematicos


# pontos

t_dois_pontos = r'\:'
t_ponto_virgula = r'\;'
t_virgula = r'\,'
t_ponto = r'\.'
t_aspas = r'\"'
t_aspas_simples = r'\''

t_negacao = r'\~'


# escopo

t_abre_parentese = r'\('
t_fecha_parentese = r'\)'
t_abre_colchete = r'\['
t_fecha_colchete = r'\]'
t_abre_chave = r'\{'
t_fecha_chave = r'\}'

# comentario

t_comentario_uma_linha = r'\^[a-zA-Z-0-9]+'

# t_comentario_n_linha = r'#\*(.|\n)*?\*#'

t_ignore = ' \t'


def t_OPmath(t):
    r'[+\-*/%]'
    return t


def t_OPatr(t):
    r'\+=|-=|\*=|\\=|='
    return t


def t_OPcomp(t):
    r'[<>]=?|==|!='
    return t


def t_OPlog(t):
    r'&&|\|\|'
    return t


def t_texto(t):
    r'"(.{1,144})"'
    return t


def t_texto_errado(t):
    r'"(.{145,})"'
    return t


def t_variavel_errada(t):
    r'^[^_A-Za-z0-9]'
    return t


def t_numero_errado(t):
    r'([0-9]+\.[a-z]+[0-9]+)|([0-9]+\.[a-z]+)|([0-9]+\.[0-9]+[a-z]+)'
    return t

# expressoes regulares dos tokens complexos


def t_variavel(t):
    r'_[a-zA-Z_0-9][a-zA-Z_0-9]*'
    return t


def t_flutuante(t):
    r'([0-9]+\.[0-9]+)|([0-9]+\.[0-9]+)'
    t.value = float(t.value)
    return t


def t_inteiro(t):
    r'\b\d{1,10}\b'
    t.value = int(t.value)
    return t


def t_nova_linha(t):
    r'\n'
    t.lexer.lineno += 1


# Regra de tratamento de erros
erroslexicos = []


def t_error(t):
    erroslexicos.append(["Erro Léxico. " +
                         "Linha: " + str(t.lineno) + " - " +
                         #   "Coluna: " + str(c) + " - " +
                         "Token não reconhecido - " + str(t.value)
                         ])
    t.lexer.skip(1)


def add_lista_saida(t, c, notificacao):
    if str(notificacao) != '':
        notificacao = 'Aviso: ' + str(notificacao)

    saidas.append(["Linha: " + str(t.lineno) + " - " +
                  "Coluna: " + str(c) + " - " +
                   "Token<" + str(t.type) + "," + str(t.value) + ">" +
                   str(notificacao)
                   ])


def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1


# Build the lexer
# lexer = lex.lex()
