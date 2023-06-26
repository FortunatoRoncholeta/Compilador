
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'CASO_FOR COMPILADORES ENQUANTO FACA FIM FLUTUANTE FUNCAO IFSULDEMINAS IMPRIMIR INICIO INTEIRO LER OPatr OPatr_simples OPcomp OPlog OPmath PARA RETORNA SAIR SE SENAO SENAO_SE TEXTO abre_chave abre_colchete abre_parentese caracter_invisivel comentario_uma_linha dois_pontos fecha_chave fecha_colchete fecha_parentese flutuante ignore inteiro negacao nova_linha numero_errado ponto ponto_virgula texto texto_errado variavel variavel_errada virgula\n    statements : statements statement\n    \n    statements : statement\n    \n    statement : IFSULDEMINAS ponto_virgula INICIO ponto_virgula COMPILADORES ponto_virgula statements FIM ponto_virgula\n              | IFSULDEMINAS ponto_virgula INICIO ponto_virgula COMPILADORES ponto_virgula FIM ponto_virgula\n    \n    statement : comentario_uma_linha\n    \n    statement : INTEIRO variavel OPatr_simples inteiro ponto_virgula\n              | INTEIRO variavel OPatr_simples flutuante ponto_virgula\n              | INTEIRO variavel ponto_virgula\n              | FLUTUANTE variavel OPatr_simples flutuante ponto_virgula\n              | FLUTUANTE variavel OPatr_simples inteiro ponto_virgula\n              | FLUTUANTE variavel ponto_virgula\n              | TEXTO variavel OPatr_simples texto ponto_virgula\n              | TEXTO variavel ponto_virgula\n    \n    statement : variavel OPatr_simples inteiro ponto_virgula\n              | variavel OPatr_simples flutuante ponto_virgula\n              | variavel OPatr inteiro ponto_virgula\n              | variavel OPatr flutuante ponto_virgula\n              | variavel OPatr variavel ponto_virgula\n              | variavel OPatr_simples texto ponto_virgula\n              | variavel OPatr_simples LER abre_parentese texto fecha_parentese ponto_virgula\n              | variavel OPatr_simples LER abre_parentese variavel fecha_parentese ponto_virgula\n              | variavel OPatr_simples LER abre_parentese fecha_parentese ponto_virgula\n    \n    statement : inteiro\n               | inteiro OPmath inteiro\n               | variavel OPmath inteiro\n               | inteiro OPmath variavel\n    \n    statement : flutuante\n               | flutuante OPmath flutuante\n               | variavel OPmath flutuante\n               | flutuante OPmath variavel\n               | inteiro OPmath flutuante\n               | flutuante OPmath inteiro\n    \n    statement : IMPRIMIR abre_parentese variavel fecha_parentese ponto_virgula\n              | IMPRIMIR abre_parentese texto fecha_parentese ponto_virgula\n              | IMPRIMIR abre_parentese texto virgula variavel fecha_parentese ponto_virgula\n    \n    comparacao : variavel OPcomp variavel\n              | variavel OPcomp inteiro\n              | variavel OPcomp flutuante\n              | variavel OPcomp texto\n              | inteiro OPcomp variavel\n              | flutuante OPcomp variavel\n              | texto OPcomp variavel\n              | texto OPcomp texto\n              | inteiro OPcomp inteiro\n              | flutuante OPcomp flutuante\n    \n    comparacao : comparacao OPlog comparacao\n    \n    statement : FUNCAO abre_parentese fecha_parentese abre_chave statements fecha_chave\n    \n    statement : variavel abre_parentese fecha_parentese\n    \n    statement : SAIR ponto_virgula\n    \n    statement : RETORNA ponto_virgula\n              | RETORNA inteiro ponto_virgula\n              | RETORNA flutuante ponto_virgula\n              | RETORNA texto ponto_virgula\n    \n    statement : SE abre_parentese comparacao fecha_parentese abre_chave statements fecha_chave\n              | SE abre_parentese comparacao fecha_parentese abre_chave statements fecha_chave SENAO abre_chave statements fecha_chave\n              | SE abre_parentese comparacao fecha_parentese abre_chave statements fecha_chave SENAO_SE abre_parentese comparacao fecha_parentese abre_chave statements fecha_chave\n              | SE abre_parentese comparacao fecha_parentese abre_chave statements fecha_chave SENAO_SE abre_parentese comparacao fecha_parentese abre_chave statements fecha_chave SENAO abre_chave statements fecha_chave\n    \n    statement : ENQUANTO abre_parentese comparacao fecha_parentese abre_chave statements fecha_chave\n    '
    
_lr_action_items = {'IFSULDEMINAS':([0,1,2,4,7,8,17,30,31,39,47,48,49,50,51,52,53,54,55,57,59,63,64,65,75,76,77,79,80,81,88,97,98,102,103,104,105,106,108,109,121,122,125,127,128,129,130,132,133,134,135,136,138,141,142,144,146,148,149,150,152,153,154,],[3,3,-2,-5,-23,-27,-1,-49,-50,-8,-48,-25,-29,-24,-26,-31,-28,-30,-32,-11,-13,-51,-52,-53,-14,-15,-19,-18,-16,-17,3,-6,-7,-9,-10,-12,-33,-34,3,3,3,3,-22,-47,3,3,3,-21,-20,-35,-54,-58,-4,-3,3,3,-55,3,3,-56,3,3,-57,]),'comentario_uma_linha':([0,1,2,4,7,8,17,30,31,39,47,48,49,50,51,52,53,54,55,57,59,63,64,65,75,76,77,79,80,81,88,97,98,102,103,104,105,106,108,109,121,122,125,127,128,129,130,132,133,134,135,136,138,141,142,144,146,148,149,150,152,153,154,],[4,4,-2,-5,-23,-27,-1,-49,-50,-8,-48,-25,-29,-24,-26,-31,-28,-30,-32,-11,-13,-51,-52,-53,-14,-15,-19,-18,-16,-17,4,-6,-7,-9,-10,-12,-33,-34,4,4,4,4,-22,-47,4,4,4,-21,-20,-35,-54,-58,-4,-3,4,4,-55,4,4,-56,4,4,-57,]),'INTEIRO':([0,1,2,4,7,8,17,30,31,39,47,48,49,50,51,52,53,54,55,57,59,63,64,65,75,76,77,79,80,81,88,97,98,102,103,104,105,106,108,109,121,122,125,127,128,129,130,132,133,134,135,136,138,141,142,144,146,148,149,150,152,153,154,],[5,5,-2,-5,-23,-27,-1,-49,-50,-8,-48,-25,-29,-24,-26,-31,-28,-30,-32,-11,-13,-51,-52,-53,-14,-15,-19,-18,-16,-17,5,-6,-7,-9,-10,-12,-33,-34,5,5,5,5,-22,-47,5,5,5,-21,-20,-35,-54,-58,-4,-3,5,5,-55,5,5,-56,5,5,-57,]),'FLUTUANTE':([0,1,2,4,7,8,17,30,31,39,47,48,49,50,51,52,53,54,55,57,59,63,64,65,75,76,77,79,80,81,88,97,98,102,103,104,105,106,108,109,121,122,125,127,128,129,130,132,133,134,135,136,138,141,142,144,146,148,149,150,152,153,154,],[9,9,-2,-5,-23,-27,-1,-49,-50,-8,-48,-25,-29,-24,-26,-31,-28,-30,-32,-11,-13,-51,-52,-53,-14,-15,-19,-18,-16,-17,9,-6,-7,-9,-10,-12,-33,-34,9,9,9,9,-22,-47,9,9,9,-21,-20,-35,-54,-58,-4,-3,9,9,-55,9,9,-56,9,9,-57,]),'TEXTO':([0,1,2,4,7,8,17,30,31,39,47,48,49,50,51,52,53,54,55,57,59,63,64,65,75,76,77,79,80,81,88,97,98,102,103,104,105,106,108,109,121,122,125,127,128,129,130,132,133,134,135,136,138,141,142,144,146,148,149,150,152,153,154,],[10,10,-2,-5,-23,-27,-1,-49,-50,-8,-48,-25,-29,-24,-26,-31,-28,-30,-32,-11,-13,-51,-52,-53,-14,-15,-19,-18,-16,-17,10,-6,-7,-9,-10,-12,-33,-34,10,10,10,10,-22,-47,10,10,10,-21,-20,-35,-54,-58,-4,-3,10,10,-55,10,10,-56,10,10,-57,]),'variavel':([0,1,2,4,5,7,8,9,10,17,21,24,25,28,30,31,35,36,39,47,48,49,50,51,52,53,54,55,57,59,63,64,65,75,76,77,78,79,80,81,87,88,90,91,92,93,94,97,98,102,103,104,105,106,108,109,121,122,125,127,128,129,130,132,133,134,135,136,138,141,142,143,144,146,148,149,150,152,153,154,],[6,6,-2,-5,19,-23,-27,26,27,-1,44,51,54,60,-49,-50,67,67,-8,-48,-25,-29,-24,-26,-31,-28,-30,-32,-11,-13,-51,-52,-53,-14,-15,-19,99,-18,-16,-17,107,6,67,111,116,118,120,-6,-7,-9,-10,-12,-33,-34,6,6,6,6,-22,-47,6,6,6,-21,-20,-35,-54,-58,-4,-3,6,67,6,-55,6,6,-56,6,6,-57,]),'inteiro':([0,1,2,4,7,8,14,17,20,21,23,24,25,30,31,35,36,38,39,47,48,49,50,51,52,53,54,55,56,57,59,63,64,65,75,76,77,79,80,81,88,90,91,92,97,98,102,103,104,105,106,108,109,121,122,125,127,128,129,130,132,133,134,135,136,138,141,142,143,144,146,148,149,150,152,153,154,],[7,7,-2,-5,-23,-27,32,-1,40,45,48,50,55,-49,-50,68,68,73,-8,-48,-25,-29,-24,-26,-31,-28,-30,-32,83,-11,-13,-51,-52,-53,-14,-15,-19,-18,-16,-17,7,68,112,115,-6,-7,-9,-10,-12,-33,-34,7,7,7,7,-22,-47,7,7,7,-21,-20,-35,-54,-58,-4,-3,7,68,7,-55,7,7,-56,7,7,-57,]),'flutuante':([0,1,2,4,7,8,14,17,20,21,23,24,25,30,31,35,36,38,39,47,48,49,50,51,52,53,54,55,56,57,59,63,64,65,75,76,77,79,80,81,88,90,91,93,97,98,102,103,104,105,106,108,109,121,122,125,127,128,129,130,132,133,134,135,136,138,141,142,143,144,146,148,149,150,152,153,154,],[8,8,-2,-5,-23,-27,33,-1,41,46,49,52,53,-49,-50,69,69,74,-8,-48,-25,-29,-24,-26,-31,-28,-30,-32,82,-11,-13,-51,-52,-53,-14,-15,-19,-18,-16,-17,8,69,113,117,-6,-7,-9,-10,-12,-33,-34,8,8,8,8,-22,-47,8,8,8,-21,-20,-35,-54,-58,-4,-3,8,69,8,-55,8,8,-56,8,8,-57,]),'IMPRIMIR':([0,1,2,4,7,8,17,30,31,39,47,48,49,50,51,52,53,54,55,57,59,63,64,65,75,76,77,79,80,81,88,97,98,102,103,104,105,106,108,109,121,122,125,127,128,129,130,132,133,134,135,136,138,141,142,144,146,148,149,150,152,153,154,],[11,11,-2,-5,-23,-27,-1,-49,-50,-8,-48,-25,-29,-24,-26,-31,-28,-30,-32,-11,-13,-51,-52,-53,-14,-15,-19,-18,-16,-17,11,-6,-7,-9,-10,-12,-33,-34,11,11,11,11,-22,-47,11,11,11,-21,-20,-35,-54,-58,-4,-3,11,11,-55,11,11,-56,11,11,-57,]),'FUNCAO':([0,1,2,4,7,8,17,30,31,39,47,48,49,50,51,52,53,54,55,57,59,63,64,65,75,76,77,79,80,81,88,97,98,102,103,104,105,106,108,109,121,122,125,127,128,129,130,132,133,134,135,136,138,141,142,144,146,148,149,150,152,153,154,],[12,12,-2,-5,-23,-27,-1,-49,-50,-8,-48,-25,-29,-24,-26,-31,-28,-30,-32,-11,-13,-51,-52,-53,-14,-15,-19,-18,-16,-17,12,-6,-7,-9,-10,-12,-33,-34,12,12,12,12,-22,-47,12,12,12,-21,-20,-35,-54,-58,-4,-3,12,12,-55,12,12,-56,12,12,-57,]),'SAIR':([0,1,2,4,7,8,17,30,31,39,47,48,49,50,51,52,53,54,55,57,59,63,64,65,75,76,77,79,80,81,88,97,98,102,103,104,105,106,108,109,121,122,125,127,128,129,130,132,133,134,135,136,138,141,142,144,146,148,149,150,152,153,154,],[13,13,-2,-5,-23,-27,-1,-49,-50,-8,-48,-25,-29,-24,-26,-31,-28,-30,-32,-11,-13,-51,-52,-53,-14,-15,-19,-18,-16,-17,13,-6,-7,-9,-10,-12,-33,-34,13,13,13,13,-22,-47,13,13,13,-21,-20,-35,-54,-58,-4,-3,13,13,-55,13,13,-56,13,13,-57,]),'RETORNA':([0,1,2,4,7,8,17,30,31,39,47,48,49,50,51,52,53,54,55,57,59,63,64,65,75,76,77,79,80,81,88,97,98,102,103,104,105,106,108,109,121,122,125,127,128,129,130,132,133,134,135,136,138,141,142,144,146,148,149,150,152,153,154,],[14,14,-2,-5,-23,-27,-1,-49,-50,-8,-48,-25,-29,-24,-26,-31,-28,-30,-32,-11,-13,-51,-52,-53,-14,-15,-19,-18,-16,-17,14,-6,-7,-9,-10,-12,-33,-34,14,14,14,14,-22,-47,14,14,14,-21,-20,-35,-54,-58,-4,-3,14,14,-55,14,14,-56,14,14,-57,]),'SE':([0,1,2,4,7,8,17,30,31,39,47,48,49,50,51,52,53,54,55,57,59,63,64,65,75,76,77,79,80,81,88,97,98,102,103,104,105,106,108,109,121,122,125,127,128,129,130,132,133,134,135,136,138,141,142,144,146,148,149,150,152,153,154,],[15,15,-2,-5,-23,-27,-1,-49,-50,-8,-48,-25,-29,-24,-26,-31,-28,-30,-32,-11,-13,-51,-52,-53,-14,-15,-19,-18,-16,-17,15,-6,-7,-9,-10,-12,-33,-34,15,15,15,15,-22,-47,15,15,15,-21,-20,-35,-54,-58,-4,-3,15,15,-55,15,15,-56,15,15,-57,]),'ENQUANTO':([0,1,2,4,7,8,17,30,31,39,47,48,49,50,51,52,53,54,55,57,59,63,64,65,75,76,77,79,80,81,88,97,98,102,103,104,105,106,108,109,121,122,125,127,128,129,130,132,133,134,135,136,138,141,142,144,146,148,149,150,152,153,154,],[16,16,-2,-5,-23,-27,-1,-49,-50,-8,-48,-25,-29,-24,-26,-31,-28,-30,-32,-11,-13,-51,-52,-53,-14,-15,-19,-18,-16,-17,16,-6,-7,-9,-10,-12,-33,-34,16,16,16,16,-22,-47,16,16,16,-21,-20,-35,-54,-58,-4,-3,16,16,-55,16,16,-56,16,16,-57,]),'$end':([1,2,4,7,8,17,30,31,39,47,48,49,50,51,52,53,54,55,57,59,63,64,65,75,76,77,79,80,81,97,98,102,103,104,105,106,125,127,132,133,134,135,136,138,141,146,150,154,],[0,-2,-5,-23,-27,-1,-49,-50,-8,-48,-25,-29,-24,-26,-31,-28,-30,-32,-11,-13,-51,-52,-53,-14,-15,-19,-18,-16,-17,-6,-7,-9,-10,-12,-33,-34,-22,-47,-21,-20,-35,-54,-58,-4,-3,-55,-56,-57,]),'fecha_chave':([2,4,7,8,17,30,31,39,47,48,49,50,51,52,53,54,55,57,59,63,64,65,75,76,77,79,80,81,97,98,102,103,104,105,106,108,125,127,128,129,132,133,134,135,136,138,141,144,146,149,150,153,154,],[-2,-5,-23,-27,-1,-49,-50,-8,-48,-25,-29,-24,-26,-31,-28,-30,-32,-11,-13,-51,-52,-53,-14,-15,-19,-18,-16,-17,-6,-7,-9,-10,-12,-33,-34,127,-22,-47,135,136,-21,-20,-35,-54,-58,-4,-3,146,-55,150,-56,154,-57,]),'FIM':([2,4,7,8,17,30,31,39,47,48,49,50,51,52,53,54,55,57,59,63,64,65,75,76,77,79,80,81,97,98,102,103,104,105,106,122,125,127,130,132,133,134,135,136,138,141,146,150,154,],[-2,-5,-23,-27,-1,-49,-50,-8,-48,-25,-29,-24,-26,-31,-28,-30,-32,-11,-13,-51,-52,-53,-14,-15,-19,-18,-16,-17,-6,-7,-9,-10,-12,-33,-34,131,-22,-47,137,-21,-20,-35,-54,-58,-4,-3,-55,-56,-57,]),'ponto_virgula':([3,13,14,19,26,27,32,33,34,37,40,41,42,44,45,46,73,74,82,83,84,85,86,96,101,123,124,126,131,137,],[18,30,31,39,57,59,63,64,65,72,75,76,77,79,80,81,97,98,102,103,104,105,106,122,125,132,133,134,138,141,]),'OPatr_simples':([6,19,26,27,],[20,38,56,58,]),'OPatr':([6,],[21,]),'OPmath':([6,7,8,],[23,24,25,]),'abre_parentese':([6,11,12,15,16,43,140,],[22,28,29,35,36,78,143,]),'texto':([14,20,28,35,36,58,78,90,91,94,143,],[34,42,61,70,70,84,100,70,114,119,70,]),'INICIO':([18,],[37,]),'LER':([20,],[43,]),'fecha_parentese':([22,29,60,61,66,71,78,99,100,107,110,111,112,113,114,115,116,117,118,119,120,145,],[47,62,85,86,89,95,101,123,124,126,-46,-36,-37,-38,-39,-44,-40,-45,-41,-43,-42,147,]),'virgula':([61,],[87,]),'abre_chave':([62,89,95,139,147,151,],[88,109,121,142,148,152,]),'OPlog':([66,71,110,111,112,113,114,115,116,117,118,119,120,145,],[90,90,90,-36,-37,-38,-39,-44,-40,-45,-41,-43,-42,90,]),'OPcomp':([67,68,69,70,],[91,92,93,94,]),'COMPILADORES':([72,],[96,]),'SENAO':([135,150,],[139,151,]),'SENAO_SE':([135,],[140,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statements':([0,88,109,121,122,142,148,152,],[1,108,128,129,130,144,149,153,]),'statement':([0,1,88,108,109,121,122,128,129,130,142,144,148,149,152,153,],[2,17,2,17,2,2,2,17,17,17,2,17,2,17,2,17,]),'comparacao':([35,36,90,143,],[66,71,110,145,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statements","S'",1,None,None,None),
  ('statements -> statements statement','statements',2,'p_statements_multiple','sintatico.py',20),
  ('statements -> statement','statements',1,'p_statements_single','sintatico.py',25),
  ('statement -> IFSULDEMINAS ponto_virgula INICIO ponto_virgula COMPILADORES ponto_virgula statements FIM ponto_virgula','statement',9,'p_statement_codigo','sintatico.py',31),
  ('statement -> IFSULDEMINAS ponto_virgula INICIO ponto_virgula COMPILADORES ponto_virgula FIM ponto_virgula','statement',8,'p_statement_codigo','sintatico.py',32),
  ('statement -> comentario_uma_linha','statement',1,'p_statement_comentario_uma_linha','sintatico.py',37),
  ('statement -> INTEIRO variavel OPatr_simples inteiro ponto_virgula','statement',5,'p_statement_declaracao_variavel','sintatico.py',42),
  ('statement -> INTEIRO variavel OPatr_simples flutuante ponto_virgula','statement',5,'p_statement_declaracao_variavel','sintatico.py',43),
  ('statement -> INTEIRO variavel ponto_virgula','statement',3,'p_statement_declaracao_variavel','sintatico.py',44),
  ('statement -> FLUTUANTE variavel OPatr_simples flutuante ponto_virgula','statement',5,'p_statement_declaracao_variavel','sintatico.py',45),
  ('statement -> FLUTUANTE variavel OPatr_simples inteiro ponto_virgula','statement',5,'p_statement_declaracao_variavel','sintatico.py',46),
  ('statement -> FLUTUANTE variavel ponto_virgula','statement',3,'p_statement_declaracao_variavel','sintatico.py',47),
  ('statement -> TEXTO variavel OPatr_simples texto ponto_virgula','statement',5,'p_statement_declaracao_variavel','sintatico.py',48),
  ('statement -> TEXTO variavel ponto_virgula','statement',3,'p_statement_declaracao_variavel','sintatico.py',49),
  ('statement -> variavel OPatr_simples inteiro ponto_virgula','statement',4,'p_statement_atribuicao_variavel','sintatico.py',54),
  ('statement -> variavel OPatr_simples flutuante ponto_virgula','statement',4,'p_statement_atribuicao_variavel','sintatico.py',55),
  ('statement -> variavel OPatr inteiro ponto_virgula','statement',4,'p_statement_atribuicao_variavel','sintatico.py',56),
  ('statement -> variavel OPatr flutuante ponto_virgula','statement',4,'p_statement_atribuicao_variavel','sintatico.py',57),
  ('statement -> variavel OPatr variavel ponto_virgula','statement',4,'p_statement_atribuicao_variavel','sintatico.py',58),
  ('statement -> variavel OPatr_simples texto ponto_virgula','statement',4,'p_statement_atribuicao_variavel','sintatico.py',59),
  ('statement -> variavel OPatr_simples LER abre_parentese texto fecha_parentese ponto_virgula','statement',7,'p_statement_atribuicao_variavel','sintatico.py',60),
  ('statement -> variavel OPatr_simples LER abre_parentese variavel fecha_parentese ponto_virgula','statement',7,'p_statement_atribuicao_variavel','sintatico.py',61),
  ('statement -> variavel OPatr_simples LER abre_parentese fecha_parentese ponto_virgula','statement',6,'p_statement_atribuicao_variavel','sintatico.py',62),
  ('statement -> inteiro','statement',1,'p_statement_inteiro','sintatico.py',67),
  ('statement -> inteiro OPmath inteiro','statement',3,'p_statement_inteiro','sintatico.py',68),
  ('statement -> variavel OPmath inteiro','statement',3,'p_statement_inteiro','sintatico.py',69),
  ('statement -> inteiro OPmath variavel','statement',3,'p_statement_inteiro','sintatico.py',70),
  ('statement -> flutuante','statement',1,'p_statement_flutuante','sintatico.py',75),
  ('statement -> flutuante OPmath flutuante','statement',3,'p_statement_flutuante','sintatico.py',76),
  ('statement -> variavel OPmath flutuante','statement',3,'p_statement_flutuante','sintatico.py',77),
  ('statement -> flutuante OPmath variavel','statement',3,'p_statement_flutuante','sintatico.py',78),
  ('statement -> inteiro OPmath flutuante','statement',3,'p_statement_flutuante','sintatico.py',79),
  ('statement -> flutuante OPmath inteiro','statement',3,'p_statement_flutuante','sintatico.py',80),
  ('statement -> IMPRIMIR abre_parentese variavel fecha_parentese ponto_virgula','statement',5,'p_statement_IMPRIMIR','sintatico.py',85),
  ('statement -> IMPRIMIR abre_parentese texto fecha_parentese ponto_virgula','statement',5,'p_statement_IMPRIMIR','sintatico.py',86),
  ('statement -> IMPRIMIR abre_parentese texto virgula variavel fecha_parentese ponto_virgula','statement',7,'p_statement_IMPRIMIR','sintatico.py',87),
  ('comparacao -> variavel OPcomp variavel','comparacao',3,'p_statement_comparacao','sintatico.py',92),
  ('comparacao -> variavel OPcomp inteiro','comparacao',3,'p_statement_comparacao','sintatico.py',93),
  ('comparacao -> variavel OPcomp flutuante','comparacao',3,'p_statement_comparacao','sintatico.py',94),
  ('comparacao -> variavel OPcomp texto','comparacao',3,'p_statement_comparacao','sintatico.py',95),
  ('comparacao -> inteiro OPcomp variavel','comparacao',3,'p_statement_comparacao','sintatico.py',96),
  ('comparacao -> flutuante OPcomp variavel','comparacao',3,'p_statement_comparacao','sintatico.py',97),
  ('comparacao -> texto OPcomp variavel','comparacao',3,'p_statement_comparacao','sintatico.py',98),
  ('comparacao -> texto OPcomp texto','comparacao',3,'p_statement_comparacao','sintatico.py',99),
  ('comparacao -> inteiro OPcomp inteiro','comparacao',3,'p_statement_comparacao','sintatico.py',100),
  ('comparacao -> flutuante OPcomp flutuante','comparacao',3,'p_statement_comparacao','sintatico.py',101),
  ('comparacao -> comparacao OPlog comparacao','comparacao',3,'p_statement_comparacao_aninhada','sintatico.py',106),
  ('statement -> FUNCAO abre_parentese fecha_parentese abre_chave statements fecha_chave','statement',6,'p_statement_declara_funcao','sintatico.py',111),
  ('statement -> variavel abre_parentese fecha_parentese','statement',3,'p_statement_chama_funcao','sintatico.py',116),
  ('statement -> SAIR ponto_virgula','statement',2,'p_statement_SAIR','sintatico.py',121),
  ('statement -> RETORNA ponto_virgula','statement',2,'p_statement_RETORNA','sintatico.py',126),
  ('statement -> RETORNA inteiro ponto_virgula','statement',3,'p_statement_RETORNA','sintatico.py',127),
  ('statement -> RETORNA flutuante ponto_virgula','statement',3,'p_statement_RETORNA','sintatico.py',128),
  ('statement -> RETORNA texto ponto_virgula','statement',3,'p_statement_RETORNA','sintatico.py',129),
  ('statement -> SE abre_parentese comparacao fecha_parentese abre_chave statements fecha_chave','statement',7,'p_statement_SE','sintatico.py',134),
  ('statement -> SE abre_parentese comparacao fecha_parentese abre_chave statements fecha_chave SENAO abre_chave statements fecha_chave','statement',11,'p_statement_SE','sintatico.py',135),
  ('statement -> SE abre_parentese comparacao fecha_parentese abre_chave statements fecha_chave SENAO_SE abre_parentese comparacao fecha_parentese abre_chave statements fecha_chave','statement',14,'p_statement_SE','sintatico.py',136),
  ('statement -> SE abre_parentese comparacao fecha_parentese abre_chave statements fecha_chave SENAO_SE abre_parentese comparacao fecha_parentese abre_chave statements fecha_chave SENAO abre_chave statements fecha_chave','statement',18,'p_statement_SE','sintatico.py',137),
  ('statement -> ENQUANTO abre_parentese comparacao fecha_parentese abre_chave statements fecha_chave','statement',7,'p_statement_ENQUANTO','sintatico.py',142),
]
