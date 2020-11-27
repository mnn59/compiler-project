
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftEQNEGELEGTLTleftANDORleftSUMSUBleftMULDIVAND ASSIGN BOOLEAN COLON COMMA DIV ELSE ELSEIF EQ ERROR FALSE FLOAT FLOATNUMBER FOR FUNCTION GE GT ID IF IN INTEGER INTEGERNUMBER LCB LE LRB LSB LT MAIN MOD MUL NE NOT ON OR PRINT RCB RETURN RRB RSB SEMICOLON SUB SUM TRUE WHERE WHILEprogram : declist MAIN LRB RRB blockdeclist : decdeclist : declist decdeclist : emptydec : vardecdec : funcdectype : INTEGERtype : FLOATtype : BOOLEANiddec : IDiddec : ID LSB expression RSBiddec : ID ASSIGN expressionidlist : iddecidlist : idlist COMMA iddecvardec : idlist COLON type SEMICOLONfuncdec : FUNCTION LRB paramdecs RRB COLON type blockfuncdec : FUNCTION ID LRB paramdecs RRB blockparamdecs : paramdecslistparamdecs : emptyparamdecslist : paramdecparamdecslist : paramdecslist COMMA paramdecparamdec : ID COLON typeparamdec : ID LSB RSB COLON typeexpression : lvalueexpression : lvalue ASSIGN expressionexpression : ID LRB explist RRBexpression : ID LRB RRBexpression : SUB expressionexpression : LRB expression RRBexpression : NOT expressionexpression : expression SUM termexpression : expression SUB termexpression : expression AND termexpression : expression OR termexpression : termterm : term MUL factorterm : term DIV factorterm : term MOD factorterm : factorfactor : INTEGERNUMBERfactor : FLOATNUMBERfactor : TRUEfactor : FALSEfactor : LRB expression RRBexpression : expression EQ expressionexpression : expression GT expressionexpression : expression GE expressionexpression : expression LT expressionexpression : expression LE expressionexpression : expression NE expressionlvalue : IDlvalue : ID LSB expression RSBblock : LCB stmtlist RCBstmt : blockstmt : vardecstmt : WHILE LRB expression RRB stmtstmt : ON LRB expression RRB LCB cases RCB SEMICOLONstmt : PRINT LRB ID RRB SEMICOLONstmt : RETURN expression SEMICOLONstmt : expression SEMICOLONstmtlist : stmtstmtlist : emptystmtlist : stmtlist stmtcase : WHERE factor COLON stmtlistcases : casecases : cases casecases : emptyexplist : expressionexplist : explist COMMA expressionempty :'
    
_lr_action_items = {'MAIN':([0,2,3,4,5,6,12,45,111,116,124,],[-70,11,-2,-4,-5,-6,-3,-15,-17,-53,-16,]),'FUNCTION':([0,2,3,4,5,6,12,45,111,116,124,],[8,8,-2,-4,-5,-6,-3,-15,-17,-53,-16,]),'ID':([0,2,3,4,5,6,8,12,14,15,17,18,30,34,35,36,45,47,51,52,58,59,60,61,62,63,64,72,83,98,99,100,101,102,108,111,113,116,117,118,119,120,121,122,124,132,133,137,139,147,148,149,],[9,9,-2,-4,-5,-6,16,-3,9,29,31,31,29,31,31,31,-15,29,31,31,31,31,31,31,31,31,31,107,31,107,-61,-62,-54,-55,31,-17,31,-53,-63,31,-60,31,130,31,-16,-59,107,-56,-58,-57,107,107,]),'$end':([1,71,116,],[0,-1,-53,]),'COLON':([7,9,10,24,29,31,33,37,38,39,40,41,42,43,46,53,66,67,76,79,82,84,85,86,87,88,89,90,91,92,93,94,95,96,97,107,112,114,127,136,146,],[13,-10,-13,-14,48,-51,-24,-35,-39,-40,-41,-42,-43,-12,73,-11,-28,-30,110,-27,-31,-32,-33,-34,-45,-46,-47,-48,-49,-50,-25,-29,-36,-37,-38,-10,-26,-52,-44,-11,148,]),'COMMA':([7,9,10,21,22,23,24,26,28,31,33,37,38,39,40,41,42,43,53,66,67,74,75,78,79,80,82,84,85,86,87,88,89,90,91,92,93,94,95,96,97,107,112,114,125,126,127,136,],[14,-10,-13,-7,-8,-9,-14,47,-20,-51,-24,-35,-39,-40,-41,-42,-43,-12,-11,-28,-30,-21,-22,113,-27,-68,-31,-32,-33,-34,-45,-46,-47,-48,-49,-50,-25,-29,-36,-37,-38,-10,-26,-52,-23,-69,-44,-11,]),'LRB':([8,11,16,17,18,31,34,35,36,45,51,52,54,55,56,57,58,59,60,61,62,63,64,68,69,70,72,83,98,99,100,101,102,103,105,106,107,108,113,116,117,118,119,120,122,132,133,137,139,143,147,148,149,],[15,19,30,34,34,51,34,34,34,-15,34,34,83,83,83,83,34,34,34,34,34,34,34,83,83,83,34,34,34,-61,-62,-54,-55,118,120,121,51,34,34,-53,-63,34,-60,34,34,-59,34,-56,-58,83,-57,34,34,]),'LSB':([9,29,31,107,],[17,49,52,122,]),'ASSIGN':([9,31,33,107,114,136,],[18,-51,64,18,-52,-52,]),'INTEGER':([13,48,73,110,],[21,21,21,21,]),'FLOAT':([13,48,73,110,],[22,22,22,22,]),'BOOLEAN':([13,48,73,110,],[23,23,23,23,]),'RRB':([15,19,21,22,23,25,26,27,28,30,31,33,37,38,39,40,41,42,50,51,65,66,67,74,75,78,79,80,82,84,85,86,87,88,89,90,91,92,93,94,95,96,97,112,114,115,125,126,127,128,129,130,],[-70,44,-7,-8,-9,46,-18,-19,-20,-70,-51,-24,-35,-39,-40,-41,-42,-43,77,79,94,-28,-30,-21,-22,112,-27,-68,-31,-32,-33,-34,-45,-46,-47,-48,-49,-50,-25,-29,-36,-37,-38,-26,-52,127,-23,-69,-44,133,134,135,]),'SUB':([17,18,31,32,33,34,35,36,37,38,39,40,41,42,43,45,51,52,58,59,60,61,62,63,64,65,66,67,72,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,104,107,108,112,113,114,115,116,117,118,119,120,122,123,126,127,128,129,131,132,133,136,137,139,147,148,149,],[35,35,-51,55,-24,35,35,35,-35,-39,-40,-41,-42,-43,55,-15,35,35,35,35,35,35,35,35,35,55,-28,55,35,-27,55,55,-31,35,-32,-33,-34,55,55,55,55,55,55,55,-29,-36,-37,-38,35,-61,-62,-54,-55,55,-51,35,-26,35,-52,55,-53,-63,35,-60,35,35,55,55,-44,55,55,55,-59,35,-52,-56,-58,-57,35,35,]),'NOT':([17,18,34,35,36,45,51,52,58,59,60,61,62,63,64,72,83,98,99,100,101,102,108,113,116,117,118,119,120,122,132,133,137,139,147,148,149,],[36,36,36,36,36,-15,36,36,36,36,36,36,36,36,36,36,36,36,-61,-62,-54,-55,36,36,-53,-63,36,-60,36,36,-59,36,-56,-58,-57,36,36,]),'INTEGERNUMBER':([17,18,34,35,36,45,51,52,54,55,56,57,58,59,60,61,62,63,64,68,69,70,72,83,98,99,100,101,102,108,113,116,117,118,119,120,122,132,133,137,139,143,147,148,149,],[39,39,39,39,39,-15,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,-61,-62,-54,-55,39,39,-53,-63,39,-60,39,39,-59,39,-56,-58,39,-57,39,39,]),'FLOATNUMBER':([17,18,34,35,36,45,51,52,54,55,56,57,58,59,60,61,62,63,64,68,69,70,72,83,98,99,100,101,102,108,113,116,117,118,119,120,122,132,133,137,139,143,147,148,149,],[40,40,40,40,40,-15,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,-61,-62,-54,-55,40,40,-53,-63,40,-60,40,40,-59,40,-56,-58,40,-57,40,40,]),'TRUE':([17,18,34,35,36,45,51,52,54,55,56,57,58,59,60,61,62,63,64,68,69,70,72,83,98,99,100,101,102,108,113,116,117,118,119,120,122,132,133,137,139,143,147,148,149,],[41,41,41,41,41,-15,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,-61,-62,-54,-55,41,41,-53,-63,41,-60,41,41,-59,41,-56,-58,41,-57,41,41,]),'FALSE':([17,18,34,35,36,45,51,52,54,55,56,57,58,59,60,61,62,63,64,68,69,70,72,83,98,99,100,101,102,108,113,116,117,118,119,120,122,132,133,137,139,143,147,148,149,],[42,42,42,42,42,-15,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,-61,-62,-54,-55,42,42,-53,-63,42,-60,42,42,-59,42,-56,-58,42,-57,42,42,]),'SEMICOLON':([20,21,22,23,31,33,37,38,39,40,41,42,66,67,79,82,84,85,86,87,88,89,90,91,92,93,94,95,96,97,104,107,112,114,123,127,135,136,144,],[45,-7,-8,-9,-51,-24,-35,-39,-40,-41,-42,-43,-28,-30,-27,-31,-32,-33,-34,-45,-46,-47,-48,-49,-50,-25,-29,-36,-37,-38,119,-51,-26,-52,132,-44,139,-52,147,]),'LCB':([21,22,23,44,45,72,77,98,99,100,101,102,109,116,117,119,132,133,134,137,139,147,148,149,],[-7,-8,-9,72,-15,72,72,72,-61,-62,-54,-55,72,-53,-63,-60,-59,72,138,-56,-58,-57,72,72,]),'RSB':([31,32,33,37,38,39,40,41,42,49,66,67,79,81,82,84,85,86,87,88,89,90,91,92,93,94,95,96,97,112,114,127,131,],[-51,53,-24,-35,-39,-40,-41,-42,-43,76,-28,-30,-27,114,-31,-32,-33,-34,-45,-46,-47,-48,-49,-50,-25,-29,-36,-37,-38,-26,-52,-44,136,]),'SUM':([31,32,33,37,38,39,40,41,42,43,65,66,67,79,80,81,82,84,85,86,87,88,89,90,91,92,93,94,95,96,97,104,107,112,114,115,123,126,127,128,129,131,136,],[-51,54,-24,-35,-39,-40,-41,-42,-43,54,54,-28,54,-27,54,54,-31,-32,-33,-34,54,54,54,54,54,54,54,-29,-36,-37,-38,54,-51,-26,-52,54,54,54,-44,54,54,54,-52,]),'AND':([31,32,33,37,38,39,40,41,42,43,65,66,67,79,80,81,82,84,85,86,87,88,89,90,91,92,93,94,95,96,97,104,107,112,114,115,123,126,127,128,129,131,136,],[-51,56,-24,-35,-39,-40,-41,-42,-43,56,56,-28,56,-27,56,56,-31,-32,-33,-34,56,56,56,56,56,56,56,-29,-36,-37,-38,56,-51,-26,-52,56,56,56,-44,56,56,56,-52,]),'OR':([31,32,33,37,38,39,40,41,42,43,65,66,67,79,80,81,82,84,85,86,87,88,89,90,91,92,93,94,95,96,97,104,107,112,114,115,123,126,127,128,129,131,136,],[-51,57,-24,-35,-39,-40,-41,-42,-43,57,57,-28,57,-27,57,57,-31,-32,-33,-34,57,57,57,57,57,57,57,-29,-36,-37,-38,57,-51,-26,-52,57,57,57,-44,57,57,57,-52,]),'EQ':([31,32,33,37,38,39,40,41,42,43,65,66,67,79,80,81,82,84,85,86,87,88,89,90,91,92,93,94,95,96,97,104,107,112,114,115,123,126,127,128,129,131,136,],[-51,58,-24,-35,-39,-40,-41,-42,-43,58,58,-28,58,-27,58,58,-31,-32,-33,-34,-45,-46,-47,-48,-49,-50,58,-29,-36,-37,-38,58,-51,-26,-52,58,58,58,-44,58,58,58,-52,]),'GT':([31,32,33,37,38,39,40,41,42,43,65,66,67,79,80,81,82,84,85,86,87,88,89,90,91,92,93,94,95,96,97,104,107,112,114,115,123,126,127,128,129,131,136,],[-51,59,-24,-35,-39,-40,-41,-42,-43,59,59,-28,59,-27,59,59,-31,-32,-33,-34,-45,-46,-47,-48,-49,-50,59,-29,-36,-37,-38,59,-51,-26,-52,59,59,59,-44,59,59,59,-52,]),'GE':([31,32,33,37,38,39,40,41,42,43,65,66,67,79,80,81,82,84,85,86,87,88,89,90,91,92,93,94,95,96,97,104,107,112,114,115,123,126,127,128,129,131,136,],[-51,60,-24,-35,-39,-40,-41,-42,-43,60,60,-28,60,-27,60,60,-31,-32,-33,-34,-45,-46,-47,-48,-49,-50,60,-29,-36,-37,-38,60,-51,-26,-52,60,60,60,-44,60,60,60,-52,]),'LT':([31,32,33,37,38,39,40,41,42,43,65,66,67,79,80,81,82,84,85,86,87,88,89,90,91,92,93,94,95,96,97,104,107,112,114,115,123,126,127,128,129,131,136,],[-51,61,-24,-35,-39,-40,-41,-42,-43,61,61,-28,61,-27,61,61,-31,-32,-33,-34,-45,-46,-47,-48,-49,-50,61,-29,-36,-37,-38,61,-51,-26,-52,61,61,61,-44,61,61,61,-52,]),'LE':([31,32,33,37,38,39,40,41,42,43,65,66,67,79,80,81,82,84,85,86,87,88,89,90,91,92,93,94,95,96,97,104,107,112,114,115,123,126,127,128,129,131,136,],[-51,62,-24,-35,-39,-40,-41,-42,-43,62,62,-28,62,-27,62,62,-31,-32,-33,-34,-45,-46,-47,-48,-49,-50,62,-29,-36,-37,-38,62,-51,-26,-52,62,62,62,-44,62,62,62,-52,]),'NE':([31,32,33,37,38,39,40,41,42,43,65,66,67,79,80,81,82,84,85,86,87,88,89,90,91,92,93,94,95,96,97,104,107,112,114,115,123,126,127,128,129,131,136,],[-51,63,-24,-35,-39,-40,-41,-42,-43,63,63,-28,63,-27,63,63,-31,-32,-33,-34,-45,-46,-47,-48,-49,-50,63,-29,-36,-37,-38,63,-51,-26,-52,63,63,63,-44,63,63,63,-52,]),'MUL':([37,38,39,40,41,42,82,84,85,86,94,95,96,97,127,],[68,-39,-40,-41,-42,-43,68,68,68,68,-44,-36,-37,-38,-44,]),'DIV':([37,38,39,40,41,42,82,84,85,86,94,95,96,97,127,],[69,-39,-40,-41,-42,-43,69,69,69,69,-44,-36,-37,-38,-44,]),'MOD':([37,38,39,40,41,42,82,84,85,86,94,95,96,97,127,],[70,-39,-40,-41,-42,-43,70,70,70,70,-44,-36,-37,-38,-44,]),'RCB':([45,72,98,99,100,101,102,116,117,119,132,137,138,139,140,141,142,145,147,148,149,],[-15,-70,116,-61,-62,-54,-55,-53,-63,-60,-59,-56,-70,-58,144,-65,-67,-66,-57,-70,-64,]),'WHILE':([45,72,98,99,100,101,102,116,117,119,132,133,137,139,147,148,149,],[-15,103,103,-61,-62,-54,-55,-53,-63,-60,-59,103,-56,-58,-57,103,103,]),'ON':([45,72,98,99,100,101,102,116,117,119,132,133,137,139,147,148,149,],[-15,105,105,-61,-62,-54,-55,-53,-63,-60,-59,105,-56,-58,-57,105,105,]),'PRINT':([45,72,98,99,100,101,102,116,117,119,132,133,137,139,147,148,149,],[-15,106,106,-61,-62,-54,-55,-53,-63,-60,-59,106,-56,-58,-57,106,106,]),'RETURN':([45,72,98,99,100,101,102,116,117,119,132,133,137,139,147,148,149,],[-15,108,108,-61,-62,-54,-55,-53,-63,-60,-59,108,-56,-58,-57,108,108,]),'WHERE':([45,99,100,101,102,116,117,119,132,137,138,139,140,141,142,145,147,148,149,],[-15,-61,-62,-54,-55,-53,-63,-60,-59,-56,143,-58,143,-65,-67,-66,-57,-70,-64,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'declist':([0,],[2,]),'dec':([0,2,],[3,12,]),'empty':([0,15,30,72,138,148,],[4,27,27,100,142,100,]),'vardec':([0,2,72,98,133,148,149,],[5,5,102,102,102,102,102,]),'funcdec':([0,2,],[6,6,]),'idlist':([0,2,72,98,133,148,149,],[7,7,7,7,7,7,7,]),'iddec':([0,2,14,72,98,133,148,149,],[10,10,24,10,10,10,10,10,]),'type':([13,48,73,110,],[20,75,109,125,]),'paramdecs':([15,30,],[25,50,]),'paramdecslist':([15,30,],[26,26,]),'paramdec':([15,30,47,],[28,28,74,]),'expression':([17,18,34,35,36,51,52,58,59,60,61,62,63,64,72,83,98,108,113,118,120,122,133,148,149,],[32,43,65,66,67,80,81,87,88,89,90,91,92,93,104,115,104,123,126,128,129,131,104,104,104,]),'lvalue':([17,18,34,35,36,51,52,58,59,60,61,62,63,64,72,83,98,108,113,118,120,122,133,148,149,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'term':([17,18,34,35,36,51,52,54,55,56,57,58,59,60,61,62,63,64,72,83,98,108,113,118,120,122,133,148,149,],[37,37,37,37,37,37,37,82,84,85,86,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'factor':([17,18,34,35,36,51,52,54,55,56,57,58,59,60,61,62,63,64,68,69,70,72,83,98,108,113,118,120,122,133,143,148,149,],[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,95,96,97,38,38,38,38,38,38,38,38,38,146,38,38,]),'block':([44,72,77,98,109,133,148,149,],[71,101,111,101,124,101,101,101,]),'explist':([51,],[78,]),'stmtlist':([72,148,],[98,149,]),'stmt':([72,98,133,148,149,],[99,117,137,99,117,]),'cases':([138,],[140,]),'case':([138,140,],[141,145,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> declist MAIN LRB RRB block','program',5,'p_program','m_parser.py',15),
  ('declist -> dec','declist',1,'p_declist_dec','m_parser.py',21),
  ('declist -> declist dec','declist',2,'p_declist_declist_dec','m_parser.py',26),
  ('declist -> empty','declist',1,'p_declist_empty','m_parser.py',31),
  ('dec -> vardec','dec',1,'p_dec_vardec','m_parser.py',36),
  ('dec -> funcdec','dec',1,'p_dec_funcdec','m_parser.py',41),
  ('type -> INTEGER','type',1,'p_type_int','m_parser.py',47),
  ('type -> FLOAT','type',1,'p_type_float','m_parser.py',52),
  ('type -> BOOLEAN','type',1,'p_type_bool','m_parser.py',57),
  ('iddec -> ID','iddec',1,'p_iddec_id','m_parser.py',63),
  ('iddec -> ID LSB expression RSB','iddec',4,'p_iddec_id_exp','m_parser.py',68),
  ('iddec -> ID ASSIGN expression','iddec',3,'p_iddec_id_assign_exp','m_parser.py',73),
  ('idlist -> iddec','idlist',1,'p_idlist_iddec','m_parser.py',79),
  ('idlist -> idlist COMMA iddec','idlist',3,'p_idlist_comma_iddec','m_parser.py',84),
  ('vardec -> idlist COLON type SEMICOLON','vardec',4,'p_vardec','m_parser.py',90),
  ('funcdec -> FUNCTION LRB paramdecs RRB COLON type block','funcdec',7,'p_funcdec_type','m_parser.py',95),
  ('funcdec -> FUNCTION ID LRB paramdecs RRB block','funcdec',6,'p_funcdec_id','m_parser.py',103),
  ('paramdecs -> paramdecslist','paramdecs',1,'p_paramdecs_paramdecslist','m_parser.py',112),
  ('paramdecs -> empty','paramdecs',1,'p_paramdecs_empty','m_parser.py',117),
  ('paramdecslist -> paramdec','paramdecslist',1,'p_paramdecslist_paramdec','m_parser.py',122),
  ('paramdecslist -> paramdecslist COMMA paramdec','paramdecslist',3,'p_paramdecslist_comma_paramdec','m_parser.py',127),
  ('paramdec -> ID COLON type','paramdec',3,'p_paramdec_id','m_parser.py',131),
  ('paramdec -> ID LSB RSB COLON type','paramdec',5,'p_paramdec_id_bracket','m_parser.py',136),
  ('expression -> lvalue','expression',1,'p_exp_val','m_parser.py',142),
  ('expression -> lvalue ASSIGN expression','expression',3,'p_exp_val_exp','m_parser.py',147),
  ('expression -> ID LRB explist RRB','expression',4,'p_exp_id_bracket_exp','m_parser.py',152),
  ('expression -> ID LRB RRB','expression',3,'p_exp_id__bracket','m_parser.py',157),
  ('expression -> SUB expression','expression',2,'p_exp_minus_exp','m_parser.py',162),
  ('expression -> LRB expression RRB','expression',3,'p_exp_bracket_exp','m_parser.py',167),
  ('expression -> NOT expression','expression',2,'p_exp_not_exp','m_parser.py',172),
  ('expression -> expression SUM term','expression',3,'p_expression_plus','m_parser.py',177),
  ('expression -> expression SUB term','expression',3,'p_expression_minus','m_parser.py',182),
  ('expression -> expression AND term','expression',3,'p_expression_and','m_parser.py',187),
  ('expression -> expression OR term','expression',3,'p_expression_or','m_parser.py',192),
  ('expression -> term','expression',1,'p_expression_term','m_parser.py',197),
  ('term -> term MUL factor','term',3,'p_term_times','m_parser.py',202),
  ('term -> term DIV factor','term',3,'p_term_div','m_parser.py',207),
  ('term -> term MOD factor','term',3,'p_term_MOD','m_parser.py',212),
  ('term -> factor','term',1,'p_term_factor','m_parser.py',217),
  ('factor -> INTEGERNUMBER','factor',1,'p_factor_num','m_parser.py',222),
  ('factor -> FLOATNUMBER','factor',1,'p_factor_float','m_parser.py',227),
  ('factor -> TRUE','factor',1,'p_factor_true','m_parser.py',232),
  ('factor -> FALSE','factor',1,'p_factor_false','m_parser.py',237),
  ('factor -> LRB expression RRB','factor',3,'p_factor_expr','m_parser.py',242),
  ('expression -> expression EQ expression','expression',3,'p_relop_exp_eq','m_parser.py',248),
  ('expression -> expression GT expression','expression',3,'p_relop_exp_gt','m_parser.py',258),
  ('expression -> expression GE expression','expression',3,'p_relop_exp_ge','m_parser.py',263),
  ('expression -> expression LT expression','expression',3,'p_relop_exp_lt','m_parser.py',268),
  ('expression -> expression LE expression','expression',3,'p_relop_exp_le','m_parser.py',273),
  ('expression -> expression NE expression','expression',3,'p_relop_exp_ne','m_parser.py',278),
  ('lvalue -> ID','lvalue',1,'p_id_exp','m_parser.py',284),
  ('lvalue -> ID LSB expression RSB','lvalue',4,'p_id_SB','m_parser.py',289),
  ('block -> LCB stmtlist RCB','block',3,'p_block','m_parser.py',295),
  ('stmt -> block','stmt',1,'p_stmt_block','m_parser.py',301),
  ('stmt -> vardec','stmt',1,'p_stmt_vardec','m_parser.py',306),
  ('stmt -> WHILE LRB expression RRB stmt','stmt',5,'p_stmt_while','m_parser.py',311),
  ('stmt -> ON LRB expression RRB LCB cases RCB SEMICOLON','stmt',8,'p_stmt_on_cases','m_parser.py',319),
  ('stmt -> PRINT LRB ID RRB SEMICOLON','stmt',5,'p_stmt_print','m_parser.py',327),
  ('stmt -> RETURN expression SEMICOLON','stmt',3,'p_stmt_return_exp','m_parser.py',332),
  ('stmt -> expression SEMICOLON','stmt',2,'p_stmt_exp','m_parser.py',337),
  ('stmtlist -> stmt','stmtlist',1,'p_stmtlist_stmt','m_parser.py',343),
  ('stmtlist -> empty','stmtlist',1,'p_stmtlist_empty','m_parser.py',348),
  ('stmtlist -> stmtlist stmt','stmtlist',2,'p_stmtlist_stmtlist','m_parser.py',352),
  ('case -> WHERE factor COLON stmtlist','case',4,'p_case','m_parser.py',358),
  ('cases -> case','cases',1,'p_cases_case','m_parser.py',362),
  ('cases -> cases case','cases',2,'p_cases_cases','m_parser.py',367),
  ('cases -> empty','cases',1,'p_cases_empty','m_parser.py',372),
  ('explist -> expression','explist',1,'p_explist_exp','m_parser.py',377),
  ('explist -> explist COMMA expression','explist',3,'p_explist_explist','m_parser.py',382),
  ('empty -> <empty>','empty',0,'p_empty','m_parser.py',387),
]
