import ply.lex as lex  # inportaçao da biblioteca 

saidas = []
def lexico(t,erro):
    saidas.append((t.lineno,t.lexpos,t.type,t.value,erro))

        # palavras reservadas

    reversed = {
        'IFSULDEMINAS' : 'IFSULDEMINAS',
        'INICIO' : 'INICIO',
        'COMPILADORES' : 'COMPILADORES',
        'FIM' : 'FIM',
        'SE' : 'SE',
        'SENAO' : 'SENAO',
        'SENAO_SE' : 'SENAO_SE',
        'ENQUANTO' : 'ENQUANTO',
        'TENTAR_EXECUTAR' : 'TENTAR_EXECUTAR',
        'PEGAR_EXCECAO' : 'PEGAR_EXCECAO',
        'TROCAR' : 'TROCAR',
        'CASO_FOR' : 'CASO_FOR',
        'SAIR_REPETICAO' : 'SAIR_REPETICAO',
        'FUNCAO': 'FUNCAO',
        'LER' : 'LER',
        'IMPRIMIR' : 'IMPRIMIR',
        'RETORNA' : 'RETORNA',
        'SAIR_TROCA' : 'SAIR_TROCA'
    }

    tokens =[
       
        'indentificador',
        'numero',


        'operador_relacional',
        'operador_matematico',

        'atribuicao',
        'ponto_virgula', 
        'dois_ponto', 
        'virgula', 
        'ponto_final',
        'negacao', 

        'tipo',
        'valor_inteiro',
        'valor_flutuante',
        'valor_e_ou_logico',
        'incremento_decremeto',
        'atribuicao',
        'resto_divisao',
        'chave_abre',
        'chave_fecha',
        'colchete_abre',
        'colchete_fecha',
        'parentese_abre',
        'parentese_fecha',
        'texto',
        'comentario_uma_linha',
        'comentario_n_linhas',
        
        'para',
        'tentar_executar',
        'pegar_excecao',
        'trocar'
    ] + list(reversed.values())

    # expressoes regulares dos tokens simples

    #matematicos
    t_mais   = r'\+'
    t_menos   = r'-'
    t_vezes   = r'\*'
    t_dividir  = r'/'
    t_modulo = r'%'
    

    #pontos
    t_atribuicao = r'='
    t_ponto_virgula = r'\;'
    t_dois_ponto = r'\:'
    t_virgula = r'\,'
    t_ponto_final = r'\.'
    t_negacao = r'\!'

    
    # escopo 
    t_chave_abre = r'\['
    t_chave_fecha =r'\]'
    t_colchete_abre =r'\{'
    t_colchete_fecha = r'\}'
    t_parentese_abre = r'\('
    t_parentese_fechar = r'\)'

    #comentario

    t_comentario_uma_linha = r'#.*$'
    t_comentario_n_linha = r'#\*(.|\n)*?\*#'

    #expressoes regulares dos tokens complexos

    def t_identificador(self,t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        # verificando se sera, palavra reservada . caso seja maiuscula sera palavra reservada
        t.type = self.reversed.get(t.value.lower(),'indentificador')
        return lexico(t,f"nenhum")


    def t_numero(self,t):
        r'-?\d+(\.\d+)?'
        return lexico(t,f"nenhum")
    
    def t_texto(t):
        r'"[^(|\n)]*"'
        return lexico(t,f"nenhum")
    
    
