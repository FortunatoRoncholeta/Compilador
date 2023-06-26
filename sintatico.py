
    # DICAS PARA O ANALISADOR LÉXICO 29-05-2023

    # - Não ser recursivo a esquerda. 
    #     Um simbolo terminal chamar ele mesmo (A -> Aa).
    #     Exemplo Transformação: 
    #     - ANTES:    <E> := <E>+<T> | <T>
    #     - DEPOIS:   <E> := <E>+<T> | <T>; <E'> := +<T><E'> | E

    # - Para um não terminal, não possuem regras cujo lado direito comecem
    # com o mesmo terminal ou sequencia (E = E+T|Ta).
    #     Exemplo Transformação: 
    #     - ANTES:    <COMANDOIF> := 'if' AP EXPR FP BLOCO | 'if' AP EXPR FP BLOCO 'else' BLOCO.
    #     - DEPOIS:   <COMANDOIF> :=  if' AP EXPR FP BLOCO ( 'else' BLOCO | {Vazio})

saidas_sintatica = []

## STATEMENT's OBRIGATÓRIAS 
def p_statements_multiple(p):
    '''
    statements : statements statement
    '''

def p_statements_single(p):
    '''
    statements : statement
    '''

# IFSULDEMINAS, INICIO, COMPILADORES statments FIM
def p_statement_codigo(p):
    '''
    statement : IFSULDEMINAS ponto_virgula INICIO ponto_virgula COMPILADORES ponto_virgula statements FIM ponto_virgula
              | IFSULDEMINAS ponto_virgula INICIO ponto_virgula COMPILADORES ponto_virgula FIM ponto_virgula
    '''

def p_statement_comentario_uma_linha(p):
    '''
    statement : comentario_uma_linha
    '''
    
def p_statement_declaracao_variavel(p):
    '''
    statement : INTEIRO variavel OPatr_simples inteiro ponto_virgula
              | INTEIRO variavel OPatr_simples flutuante ponto_virgula
              | INTEIRO variavel ponto_virgula
              | FLUTUANTE variavel OPatr_simples flutuante ponto_virgula
              | FLUTUANTE variavel OPatr_simples inteiro ponto_virgula
              | FLUTUANTE variavel ponto_virgula
              | TEXTO variavel OPatr_simples texto ponto_virgula
              | TEXTO variavel ponto_virgula
    '''

def p_statement_atribuicao_variavel(p):
    '''
    statement : variavel OPatr_simples inteiro ponto_virgula
              | variavel OPatr_simples flutuante ponto_virgula
              | variavel OPatr inteiro ponto_virgula
              | variavel OPatr flutuante ponto_virgula
              | variavel OPatr variavel ponto_virgula
              | variavel OPatr_simples texto ponto_virgula
              | variavel OPatr_simples LER abre_parentese texto fecha_parentese ponto_virgula
              | variavel OPatr_simples LER abre_parentese variavel fecha_parentese ponto_virgula
              | variavel OPatr_simples LER abre_parentese fecha_parentese ponto_virgula
    '''

def p_statement_inteiro(p):
    '''
    statement : inteiro
               | inteiro OPmath inteiro
               | variavel OPmath inteiro
               | inteiro OPmath variavel
    '''

def p_statement_flutuante(p):
    '''
    statement : flutuante
               | flutuante OPmath flutuante
               | variavel OPmath flutuante
               | flutuante OPmath variavel
               | inteiro OPmath flutuante
               | flutuante OPmath inteiro
    '''

def p_statement_IMPRIMIR(p):
    '''
    statement : IMPRIMIR abre_parentese variavel fecha_parentese ponto_virgula
              | IMPRIMIR abre_parentese texto fecha_parentese ponto_virgula
              | IMPRIMIR abre_parentese texto virgula variavel fecha_parentese ponto_virgula
    '''

def p_statement_comparacao(p):
    '''
    comparacao : variavel OPcomp variavel
              | variavel OPcomp inteiro
              | variavel OPcomp flutuante
              | variavel OPcomp texto
              | inteiro OPcomp variavel
              | flutuante OPcomp variavel
              | texto OPcomp variavel
              | texto OPcomp texto
              | inteiro OPcomp inteiro
              | flutuante OPcomp flutuante
    '''

def p_statement_comparacao_aninhada(p):
    '''
    comparacao_aninhada : comparacao OPlog comparacao
    '''

def p_statement_declara_funcao(p): 
    '''
    statement : FUNCAO abre_parentese fecha_parentese abre_chave statements fecha_chave
    '''

def p_statement_chama_funcao(p): 
    '''
    statement : variavel abre_parentese fecha_parentese
    '''

def p_statement_SAIR(p): 
    '''
    statement : SAIR ponto_virgula
    '''  

def p_statement_RETORNA(p): 
    '''
    statement : RETORNA ponto_virgula
              | RETORNA inteiro ponto_virgula
              | RETORNA flutuante ponto_virgula
              | RETORNA texto ponto_virgula
    '''   

def p_statement_condicionais(p): 
    '''
    statement : SE abre_parentese comparacao fecha_parentese abre_chave statements fecha_chave
              | SE abre_parentese comparacao fecha_parentese abre_chave statements fecha_chave SENAO abre_chave statements fecha_chave
              | SE abre_parentese comparacao fecha_parentese abre_chave statements fecha_chave SENAO_SE abre_parentese comparacao fecha_parentese abre_chave statements fecha_chave
              | SE abre_parentese comparacao fecha_parentese abre_chave statements fecha_chave SENAO_SE abre_parentese comparacao fecha_parentese abre_chave statements fecha_chave SENAO abre_chave statements fecha_chave
    
    '''  

# def p_statement_lacos(p): 
#     '''
#     statement :ENQUANTO abre_parentese comparacao fecha_parentese abre_chave statements fecha_chave 
#               | PARA variavel EM INTERVALO abre_parentese inteiro virgula inteiro fecha_parentese abre_chave statements fecha_chave 
#               | PARA inteiro EM INTERVALO abre_parentese  inteiro virgula variavel fecha_parentese abre_chave statements fecha_chave 
#               | PARA inteiro EM INTERVALO abre_parentese  variavel virgula inteiro fecha_parentese abre_chave statements fecha_chave 
#               | PARA variavel EM INTERVALO abre_parentese variavel virgula variavel fecha_parentese abre_chave statements fecha_chave 
#               | PARA inteiro EM INTERVALO abre_parentese  variavel virgula variavel fecha_parentese abre_chave statements fecha_chave  
#     '''

errossintaticos = []
def p_error(p):

    errossintaticos.append(["Erro Sintático. " +
                         #"Linha: " + str(p.lineno) + " - " +
                         #"Coluna: " + str(c) + " - " +
                         "Gramática não reconhecida proximo ao token <" + str(p.value) + ">"
                         ])
