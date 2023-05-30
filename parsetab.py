
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'CASO_FOR COMPILADORES ENQUANTO FACA FIM FLUTUANTE FUNCAO IFSULDEMINAS IMPRIMIR INICIO LER PARA RETORNA SAIR SE SENAO SENAO_SE TEXTO TINTEIRO abre_chave abre_colchete abre_parentese aspas aspas_simples caracter_invisivel comentario_uma_linha diferente divide_igual dividir dois_pontos duplo_igual e exatamente_igual fecha_chave fecha_colchete fecha_parentese flutuante ignore igual inteiro maior maior_igual mais mais_igual menor menor_igual menos menos_igual modulo negacao numero_errado ou ponto ponto_virgula texto texto_errado variavel variavel_errada vezes vezes_igual virgula\n    statements : statements statement\n    \n    statements : statement\n    \n    statement : IFSULDEMINAS ponto_virgula\n    \n    statement : INICIO ponto_virgula\n    \n    statement : COMPILADORES ponto_virgula\n    \n    statement : FIM ponto_virgula\n    '
    
_lr_action_items = {'IFSULDEMINAS':([0,1,2,7,8,9,10,11,],[3,3,-2,-1,-3,-4,-5,-6,]),'INICIO':([0,1,2,7,8,9,10,11,],[4,4,-2,-1,-3,-4,-5,-6,]),'COMPILADORES':([0,1,2,7,8,9,10,11,],[5,5,-2,-1,-3,-4,-5,-6,]),'FIM':([0,1,2,7,8,9,10,11,],[6,6,-2,-1,-3,-4,-5,-6,]),'$end':([1,2,7,8,9,10,11,],[0,-2,-1,-3,-4,-5,-6,]),'ponto_virgula':([3,4,5,6,],[8,9,10,11,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statements':([0,],[1,]),'statement':([0,1,],[2,7,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statements","S'",1,None,None,None),
  ('statements -> statements statement','statements',2,'p_statements_multiple','sintatico.py',22),
  ('statements -> statement','statements',1,'p_statements_single','sintatico.py',27),
  ('statement -> IFSULDEMINAS ponto_virgula','statement',2,'p_statement_ifsuldeminas','sintatico.py',33),
  ('statement -> INICIO ponto_virgula','statement',2,'p_statement_inicio','sintatico.py',38),
  ('statement -> COMPILADORES ponto_virgula','statement',2,'p_statement_compiladores','sintatico.py',43),
  ('statement -> FIM ponto_virgula','statement',2,'p_statement_fim','sintatico.py',48),
]
