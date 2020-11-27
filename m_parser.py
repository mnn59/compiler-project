from lexer import Lexer
import ply.yacc as yacc


class Parser:

    tokens = Lexer().tokens

    def __init__(self):
        pass

        # Yacc example

    def p_program(self, p):
        'program : expression'
        # p[0] = p[1]
        print('program : expression')

    # declist
    def p_declist_dec(self, p):
        'declist : dec'
        p[0] = p[1]
        print('declist : dec')

    def p_declist_declist_dec(self, p):
        'declist : declist dec'
        p[0] = p[1] + p[2]
        print('declist : declist dec')

    def p_declist_empty(self, p):
        'declist : empty'
        print('declist : empty')

    # dec
    def p_dec_vardec(self, p):
        'dec : vardec'
        p[0] = p[1]
        print('dec : vardec')

    def p_dec_funcdec(self, p):
        'dec : funcdec'
        p[0] = p[1]
        print('dec : funcdec')

    # type
    def p_type_int(self, p):
        'type : INTEGER'
        p[0] = p[1]
        print('type : INTEGER')

    def p_type_float(self, p):
        'type : FLOAT'
        p[0] = p[1]
        print('type : FLOAT')

    def p_type_bool(self, p):
        'type : BOOLEAN'
        p[0] = p[1]
        print('type : BOOLEAN')

    # iddec
    def p_iddec_id(self, p):
        'iddec : ID'
        p[0] = p[1]
        print('iddec : ID')

    def p_iddec_id_exp(self, p):
        'iddec : ID LSB expression RSB'
        p[0] = f'{p[1]}[{p[3]}]'
        print('iddec : ID LSB expression RSB')
    def p_iddec_id_assign_exp(self, p):
        'iddec : ID ASSIGN expression'
        p[0] = f'{p[1]}={p[3]}'
        print('iddec : ID ASSIGN expression')

    # idlist
    def p_idlist_iddec(self, p):
        'idlist : iddec'
        p[0] = p[1]
        print('idlist : iddec')

    def p_idlist_comma_iddec(self, p):
        'idlist : idlist COMMA iddec'
        p[0] = f'{p[1]},{p[3]}'
        print('idlist : idlist COMMA iddec')



    # exp
    def p_exp_val(self, p):
        'expression : lvalue'
        # p[0] = p[1]
        print('expression : lvalue')

    def p_exp_val_exp(self, p):
        'expression : lvalue ASSIGN expression'
        # p[0] = p[1]
        print('expression : lvalue')

    def p_exp_id_bracket_exp(self, p):
        'expression : ID LRB explist RRB'
        p[0] = f'{p[1]}({p[3]})'
        print('expression : ID LRB explist RRB')

    def p_exp_id__bracket(self, p):
        'expression : ID LRB RRB'
        p[0] = f'{p[1]}()'
        print('expression : ID LRB RRB')

    def p_exp_minus_exp(self, p):
        'expression : SUB expression'
        p[0] = f'- {p[2]}'
        print('expression : SUB expression')

    def p_exp_bracket_exp(self, p):
        'expression : LRB expression RRB'
        p[0] = f'({p[2]})'
        print('expression : LRB expression RRB')

    def p_exp_not_exp(self, p):
        'expression : NOT expression'
        p[0] = p[1] + p[2]
        print('expression : NOT expression')

    def p_expression_plus(self, p):
        'expression : expression SUM term'
        p[0] = p[1] + p[3]
        print('expression : expression SUM term')

    def p_expression_minus(self, p):
        'expression : expression SUB term'
        p[0] = p[1] - p[3]
        print('expression : expression SUB term')

    def p_expression_and(self, p):
        'expression : expression AND term'
        p[0] = p[1] & p[3]
        print('expression : expression AND term')

    def p_expression_or(self, p):
        'expression : expression OR term'
        p[0] = p[1] | p[3]
        print('expression : expression OR term')

    def p_expression_term(self, p):
        'expression : term'
        p[0] = p[1]
        print('expression : term')

    def p_term_times(self, p):
        'term : term MUL factor'
        p[0] = p[1] * p[3]
        print('term : term MUL factor')

    def p_term_div(self, p):
        'term : term DIV factor'
        p[0] = p[1] / p[3]
        print('term : term DIV factor')

    def p_term_MOD(self, p):
        'term : term MOD factor'
        p[0] = p[1] % p[3]
        print('term : term MOD factor')

    def p_term_factor(self, p):
        'term : factor'
        p[0] = p[1]
        print('term : factor')

    def p_factor_num(self, p):
        'factor : INTEGERNUMBER'
        p[0] = p[1]
        print('factor : INTEGERNUMBER')

    def p_factor_float(self, p):
        'factor : FLOATNUMBER'
        p[0] = p[1]
        print('factor : FLOATNUMBER')

    def p_factor_true(self, p):
        'factor : TRUE'
        p[0] = True
        print('factor : TRUE')

    def p_factor_false(self, p):
        'factor : FALSE'
        p[0] = False
        print('factor : FALSE')

    def p_factor_expr(self, p):
        'factor : LRB expression RRB'
        p[0] = p[2]
        print('factor : LRB expression RRB')

    # relop
    def p_relop_exp_eq(self, p):
        'expression : expression EQ expression'
        p[0] = p[1] == p[3]
        print('expression : expression EQ expression')

    # def p_relop_eq(self, p):
    #     'relopexp : relopexp EQ expression'
    #     p[0] = p[1] == p[3]
    #     print('relopexp : relopexp EQ expression')

    def p_relop_exp_gt(self, p):
        'expression : expression GT expression'
        p[0] = p[1] > p[3]
        print('expression : expression GT expression')

    def p_relop_exp_ge(self, p):
        'expression : expression GE expression'
        p[0] = p[1] >= p[3]
        print('expression : expression GE expression')

    def p_relop_exp_lt(self, p):
        'expression : expression LT expression'
        p[0] = p[1] < p[3]
        print('expression : expression LT expression')

    def p_relop_exp_le(self, p):
        'expression : expression LE expression'
        p[0] = p[1] <= p[3]
        print('expression : expression LE expression')

    def p_relop_exp_ne(self, p):
        'expression : expression NE expression'
        p[0] = p[1] != p[3]
        print('expression : expression NE expression')

    # lvalue
    def p_id_exp(self, p):
        'lvalue : ID'
        p[0] = p[1]
        print('lvalue : ID')

    def p_id_SB(self, p):
        'lvalue : ID LSB expression RSB'
        p[0] = p[2]
        print('lvalue : LSB ID RSB')

    # block
    def p_block(self, p):
        'block : LCB stmtlist RCB'
        p[0] = p[2]
        print('block : LCB stmtlist RCB')

    # stmt
    def p_stmt_block(self, p):
        'stmt : block'
        p[0] = p[1]
        print('stmt : block')

    def p_stmt_print(self, p):
        'stmt : PRINT LRB ID RRB SEMICOLON'
        p[0] = f'print({p[3]});'
        print('stmt : PRINT LRB ID RRB SEMICOLON')

    def p_stmt_exp(self, p):
        'stmt : RETURN expression SEMICOLON'
        p[0] = p[2]
        print('stmt : RETURN expression SEMICOLON')

    # stmtlist
    def p_stmtlist_stmt(self, p):
        'stmtlist : stmt'
        p[0] = p[1]
        print('stmtlist : stmt')

    def p_stmtlist_empty(self, p):
        'stmtlist : empty'
        print('stmtlist : empty')

    def p_stmtlist_stmtlist(self, p):
        'stmtlist : stmtlist stmt'
        p[0] = p[1] + p[2]
        print('stmtlist : stmtlist stmt')

    # cases
    def p_case(self, p):
        'case : WHERE factor COLON stmtlist'
        print('case : WHERE factor COLON stmtlist')

    def p_cases_case(self, p):
        'cases : case'
        p[0] = p[1]
        print('cases : case')

    def p_cases_cases(self, p):
        'cases : cases case'
        p[0] = p[1] + p[2]
        print('cases : cases case')

    def p_cases_empty(self, p):
        'cases : empty'
        print('cases : empty')

    # expilst
    def p_explist_exp(self, p):
        'explist : exp'
        p[0] = p[1]
        print('explist : exp')

    def p_explist_explist(self, p):
        'explist : explist COMMA expression'
        p[0] = f'{p[1]},{p[3]}'
        print('explist : explist COMMA expression')

    def p_empty(self, p):
        'empty :'
        print('empty :')
        pass
    # def p_if_exp(self, p):
    #     'ifexp : LRB expression RRB '

    # def p_relop_gt(self, p):
    #     'relopexp : relopexp GT expression'
    #     p[0] = p[1] > p[3]
    #     print('relopexp : relopexp GT expression')

    precedence = (
        ('left', 'EQ', 'NE', 'GE', 'LE', 'GT', 'LT'),
        ('left', 'AND', 'OR'),
        ('left', 'SUM', 'SUB'),
        ('left', 'MUL', 'DIV'),
    )


    # Error rule for syntax errors
    def p_error(self, p):
        print("Syntax error in input! " + p.value )

    def build(self, **kwargs):
        self.parser = yacc.yacc(module=self, **kwargs)
        return self.parser