
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


 ## STATEMENT's OBRIGATÓRIAS 
def p_statements_multiple(p):
    '''
    statements : statements statement
    '''

def p_statements_single(p):
    '''
    statements : statement
    '''

# STATEMENT's PITÃO
# IFSULDEMINAS, INICIO, COMPILADORES, FIM
def p_statement_codigo(p):
    '''
    statement : IFSULDEMINAS ponto_virgula INICIO ponto_virgula COMPILADORES ponto_virgula statements FIM ponto_virgula
    '''

def p_statement_comentario_uma_linha(p):
    '''
    statement : comentario_uma_linha
    '''

errossintaticos = []
def p_error(p):
    errossintaticos.append(p)
    print("ERRO: ",p)
