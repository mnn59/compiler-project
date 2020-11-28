from lexer import Lexer
import ply.yacc as yacc


class Parser:

    tokens = Lexer().tokens

    def __init__(self):
        pass

        # Yacc example
    def p_program_declist(self, p):
        'program : declist MAIN LRB RRB block'
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5]
        print('program : declist MAIN LRB RRB block')

    def p_program(self, p):
        'program : MAIN LRB RRB block'
        p[0] = p[1] + p[2] + p[3] + p[4]
        print('program : MAIN LRB RRB block')

    # declist 1
    def p_declist_dec(self, p):
        'declist : dec'
        p[0] = p[1]
        print('declist : dec')

    def p_declist_declist_dec(self, p):
        'declist : declist dec'
        p[0] = p[1] + p[2]
        print('declist : declist dec')

    # block 1
    def p_block(self, p):
        'block : LCB stmtlist RCB'
        p[0] = p[1] + p[2] + p[3]
        print('block : LCB stmtlist RCB')

    def p_block_empty(self, p):
        'block : LCB RCB'
        p[0] = p[1] + p[2]
        print('block : LCB RCB')

    # dec 2
    def p_dec_vardec(self, p):
        'dec : vardec'
        p[0] = p[1]
        print('dec : vardec')

    def p_dec_funcdec(self, p):
        'dec : funcdec'
        p[0] = p[1]
        print('dec : funcdec')

    # stmtlist 2
    def p_stmtlist_stmt(self, p):
        'stmtlist : stmt'
        p[0] = p[1]
        print('stmtlist : stmt')

    def p_stmtlist_stmtlist(self, p):
        'stmtlist : stmtlist stmt'
        p[0] = p[1] + p[2]
        print('stmtlist : stmtlist stmt')

    # stmt 3
    def p_stmt_block(self, p):
        'stmt : block'
        p[0] = p[1]
        print('stmt : block')

    def p_stmt_vardec(self, p):
        'stmt : vardec'
        p[0] = p[1]
        print('stmt : vardec')

    def p_stmt_while(self, p):
        'stmt : WHILE LRB expression RRB stmt'
        temp = ''
        for i in range(1, 6):
            temp += p[i]
        p[0] = temp
        print('stmt : WHILE LRB expression RRB stmt')

    def p_stmt_on_cases(self, p):
        'stmt : ON LRB expression RRB LCB cases RCB SEMICOLON'
        temp = ''
        for i in range(1, 9):
            temp += p[i]
        p[0] = temp
        print('stmt : ON LRB expression RRB LCB cases RCB SEMICOLON')

    def p_stmt_on_cases_emsilan(self, p):
        'stmt : ON LRB expression RRB LCB RCB SEMICOLON'
        temp = ''
        for i in range(1, 8):
            temp += p[i]
        p[0] = temp
        print('stmt : ON LRB expression RRB LCB RCB SEMICOLON')

    def p_stmt_print(self, p):
        'stmt : PRINT LRB ID RRB SEMICOLON'
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5]
        print('stmt : PRINT LRB ID RRB SEMICOLON')

    def p_stmt_return_exp(self, p):
        'stmt : RETURN expression SEMICOLON'
        p[0] = p[1] + p[2] + p[3]
        print('stmt : RETURN expression SEMICOLON')

    def p_stmt_exp(self, p):
        'stmt : expression SEMICOLON'
        p[0] = p[1] + p[2]
        print('stmt : expression SEMICOLON', p[0])

    def p_stmt_for_exp(self, p):
        'stmt : FOR LRB expression SEMICOLON expression SEMICOLON expression RRB stmt'
        temp = ''
        for i in range(1, 10):
            temp += str(p[i])
        p[0] = temp
        print('stmt : FOR LRB expression SEMICOLON expression SEMICOLON expression RRB stmt')

    def p_stmt_for_id(self, p):
        'stmt : FOR LRB ID IN ID RRB stmt'
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + p[7]
        print('stmt : FOR LRB ID IN ID RRB stmt')

    def p_stmt_if(self, p):
        'stmt : IF LRB expression RRB stmt %prec SHIFT_IF'
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5]
        print('stmt : IF LRB expression RRB elseiflist')

    def p_stmt_if_2(self, p):
        'stmt : IF LRB expression RRB stmt ELSE stmt %prec SHIFT_IFELSE'
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + p[7]
        print('stmt : IF LRB expression RRB elseiflist')

    def p_stmt_if_3(self, p):
        'stmt : IF LRB expression RRB elseiflist %prec SHIFT_ELSEIFLIST'
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5]
        print('stmt : IF LRB expression RRB elseiflist')

    def p_stmt_if_4(self, p):
        'stmt : IF LRB expression RRB elseiflist ELSE stmt %prec SHIFT_ELSEIFLIST'
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + p[7]
        print('stmt : IF LRB expression RRB elseiflist')

    # def p_stmt_if_2(self, p):
    #     'stmt : IF LRB expression RRB elseiflist ELSE stmt %prec SHIFT_VARDEC'
    #     p[0] = p[1] + p[2] + p[3] + p[4] + p[5]
    #     print('stmt : IF LRB expression RRB elseiflist ELSE stmt')

    # elseiflist
    def p_elseiflist_elseif(self, p):
        'elseiflist : ELSEIF LRB expression RRB stmt'
        temp = ''
        for i in range(1, 6):
            temp += p[i]
        p[0] = temp
        print('elseiflist : ELSEIF LRB expression RRB stmt')

    def p_elseiflist_elseiflist(self, p):
        'elseiflist : elseiflist ELSEIF LRB expression RRB stmt'
        temp = ''
        for i in range(1, 7):
            temp += p[i]
        p[0] = temp
        print('elseiflist : elseiflist ELSEIF LRB expression RRB stmt')


    # def p_iftoken_smt(self, p):
    #     'iftoken : stmt emptyif %prec SHIFT_VARDEC'
    #     p[0] = p[1]
    #     print('iftoken : stmt')
    #
    # def p_iftoken_smt_elseiflist(self, p):
    #     'iftoken : stmt ELSEIF elseiflist'
    #     p[0] = p[1] + p[2] + p[3]
    #     print('iftoken : stmt')
    #
    # def p_iftokcen_smt_elseiflist_else(self, p):
    #     'iftoken : stmt ELSEIF elseiflist ELSE stmt'
    #     p[0] = p[1] + p[2] + p[3] + p[4] + p[5]
    #     print('iftoken : stmt')
    #
    # def p_iftoken_smt_else(self, p):
    #     'iftoken : stmt ELSE stmt'
    #     p[0] = p[1] + p[2] + p[3]
    #     print('iftoken : stmt ELSE stmt')

    # def p_emptyif(self, p):
    #     'emptyif : '
    #     pass


    # def p_stmt_if_exp(self, p):
    #     'stmt : IF LRB expression RRB stmt elseiflist'
    #     p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6]
    #     print('stmt : IF LRB expression RRB stmt elseiflist')
    #
    # def p_stmt_if_exp_elseiflist(self, p):
    #     'stmt : IF LRB expression RRB stmt elseiflist ELSE stmt'
    #     p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + p[7] + p[8]
    #     print('stmt : IF LRB expression RRB stmt elseiflist ELSE stmt')
    #
    # def p_stmt_if_exp_empty(self, p):
    #     'stmt : IF LRB expression RRB stmt'
    #     p[0] = p[1] + p[2] + p[3] + p[4] + p[5]
    #     print('stmt : IF LRB expression RRB stmt')
    #
    # def p_stmt_if_exp_elseiflist_empty(self, p):
    #     'stmt : IF LRB expression RRB stmt ELSE stmt'
    #     p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6] + p[7]
    #     print('stmt : IF LRB expression RRB stmt ELSE stmt')

    # vardec 3
    def p_vardec(self, p):
        'vardec : idlist COLON type SEMICOLON'
        p[0] = p[1] + p[2] + p[3] + p[4]
        print('vardec : idlist COLON type SEMICOLON')

    # funcdec 3
    def p_funcdec_type(self, p):
        'funcdec : FUNCTION ID LRB paramdecslist RRB COLON type block'
        temp = ''
        for i in range(1, 8):
            temp += p[i]
        p[0] = temp
        print('funcdec : FUNCTION ID LRB paramdecslist RRB COLON type block')

    def p_funcdec_type_empty(self, p):
        'funcdec : FUNCTION ID LRB RRB COLON type block'
        temp = ''
        for i in range(1, 7):
            temp += p[i]
        p[0] = temp
        print('funcdec : FUNCTION LRB RRB COLON type block')

    def p_funcdec_id(self, p):
        'funcdec : FUNCTION ID LRB paramdecslist RRB block'
        temp = ''
        for i in range(1, 7):
            temp += p[i]
        p[0] = temp
        print('funcdec : FUNCTION ID LRB paramdecslist RRB block')

    def p_funcdec_id_empty(self, p):
        'funcdec : FUNCTION ID LRB RRB block'
        temp = ''
        for i in range(1, 6):
            temp += p[i]
        p[0] = temp
        print('funcdec : FUNCTION ID LRB RRB block')

    # type 4
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

    # cases 4
    def p_case(self, p):
        'case : WHERE factor COLON stmtlist'
        p[0] = p[1] + p[2] + p[3] + p[4]
        print('case : WHERE factor COLON stmtlist')

    def p_case_empty_stmtlist(self, p):
        'case : WHERE factor COLON'
        p[0] = p[1] + p[2] + p[3]
        print('case : WHERE factor COLON')

    def p_cases_case(self, p):
        'cases : case'
        p[0] = p[1]
        print('cases : case')

    def p_cases_cases(self, p):
        'cases : cases case'
        for i in range(3):
            print(p[i])
        p[0] = p[1] + p[2]
        print('cases : cases case')
    #
    # def p_cases_empty(self, p):
    #     'cases : empty'
    #     print('cases : empty')

    # idlist 4
    def p_idlist_iddec(self, p):
        'idlist : iddec'
        p[0] = p[1]
        print('idlist : iddec')

    def p_idlist_comma_iddec(self, p):
        'idlist : idlist COMMA iddec'
        p[0] = p[1] + p[2] + p[3]
        print('idlist : idlist COMMA iddec')

    # # paramdecs 4
    # def p_paramdecs_paramdecslist(self, p):
    #     'paramdecs : paramdecslist'
    #     p[0] = p[1]
    #     print('paramdecs : paramdecslist')
    # # here
    # def p_paramdecs_empty(self, p):
    #     'paramdecs : empty'
    #     print('paramdecs : empty')

    # paramdecslist 5
    def p_paramdecslist_paramdec(self, p):
        'paramdecslist : paramdec'
        p[0] = p[1]
        print('paramdecslist : paramdec')

    def p_paramdecslist_comma_paramdec(self, p):
        'paramdecslist : paramdecslist COMMA paramdec'
        p[0] = p[1] + p[2] + p[3]
        print(p[0])
        print('paramdecslist : paramdecslist COMMA paramdec')

    # iddec 5
    def p_iddec_id(self, p):
        'iddec : ID %prec SHIFT_IDDEC'
        p[0] = p[1]
        print('iddec : ID')

    def p_iddec_id_exp(self, p):
        'iddec : ID LSB expression RSB'
        p[0] = p[1] + p[2] + p[3] + p[4]
        print('iddec : ID LSB expression RSB', p[0])

    def p_iddec_id_assign_exp(self, p):
        'iddec : ID ASSIGN expression %prec SHIFT_IDDEC'
        p[0] = p[1] + p[2] + p[3]
        print('iddec : ID ASSIGN expression')

    # lvalue
    def p_lvalue_id_exp(self, p):
        'lvalue : ID %prec SHIFT_LVALUE'
        p[0] = p[1]
        print('lvalue : ID')

    def p_lvalue_id_sb(self, p):
        'lvalue : ID LSB expression RSB %prec SHIFT_LVALUE'
        p[0] = p[1] + p[2] + p[3] + p[4]
        print('lvalue : ID LSB expression RSB')

    def p_exp_id_assign_sb(self,p):
        'expression : ID LSB expression RSB ASSIGN expression %prec SHIFT_ASSIGN'
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6]
        print('expression : ID LSB expression RSB ASSIGN expression')

    def p_exp_id_assign(self,p):
        'expression : ID ASSIGN expression %prec SHIFT_ASSIGN'
        p[0] = p[1] + p[2] + p[3]
        print('expression : ID ASSIGN expression %prec SHIFT_ASSIGN')

    # paramdec 6
    def p_paramdec_id(self, p):
        'paramdec : ID COLON type'
        p[0] = p[1] + p[2] + p[3]
        print('paramdec : ID COLON type')

    def p_paramdec_id_bracket(self, p):
        'paramdec : ID LSB RSB COLON type'
        p[0] = p[1] + p[2] + p[3] + p[4] + p[5]
        print('paramdec : ID LSB RSB COLON type')

    # expilst
    def p_explist_exp(self, p):
        'explist : expression'
        p[0] = p[1]
        print('explist : expression')

    def p_explist_explist(self, p):
        'explist : explist COMMA expression'
        p[0] = f'{p[1]},{p[3]}'
        print('explist : explist COMMA expression')




    # relop
    def p_relop_exp_eq(self, p):
        'expression : expression EQ expression'
        p[0] = p[1] + p[2] + p[3]
        print('expression : expression EQ expression')

    def p_relop_exp_gt(self, p):
        'expression : expression GT expression'
        p[0] = p[1] + p[2] + p[3]
        print('expression : expression GT expression')

    def p_relop_exp_ge(self, p):
        'expression : expression GE expression'
        p[0] = p[1] + p[2] + p[3]
        print('expression : expression GE expression')

    def p_relop_exp_lt(self, p):
        'expression : expression LT expression'
        p[0] = p[1] + p[2] + p[3]
        print('expression : expression LT expression')

    def p_relop_exp_le(self, p):
        'expression : expression LE expression'
        p[0] = p[1] + p[2] + p[3]
        print('expression : expression LE expression')

    def p_relop_exp_ne(self, p):
        'expression : expression NE expression'
        p[0] = p[1] + p[2] + p[3]
        print('expression : expression NE expression')

    # exp
    def p_expression_val(self, p):
        'expression : lvalue'
        p[0] = p[1]
        print('expression : lvalue', p[0])

    def p_expression_val_exp(self, p):
        'expression : lvalue ASSIGN expression'
        p[0] = p[1] + p[2] + p[3]
        print('expression : lvalue ASSIGN expression', p[0])

    def p_expression_id_bracket_exp(self, p):
        'expression : ID LRB explist RRB'
        p[0] = p[1] + p[2] + p[3] + p[4]
        print('expression : ID LRB explist RRB')

    def p_expression_id__bracket(self, p):
        'expression : ID LRB RRB'
        p[0] = p[1] + p[2] + p[3]
        print('expression : ID LRB RRB')

    def p_expression_minus_exp(self, p):
        'expression : SUB expression'
        p[0] = p[1] + p[2]
        print('expression : SUB expression')

    # def p_exp_bracket_exp(self, p):
    #     'expression : LRB expression RRB'
    #     p[0] = f'({p[2]})'
    #     print('expression : LRB expression RRB')

    def p_expression_not_exp(self, p):
        'expression : NOT expression'
        p[0] = p[1] + p[2]
        print('expression : NOT expression')

    def p_expression_plus(self, p):
        'expression : expression SUM expression'
        p[0] = p[1] + p[2] + p[3]
        print('expression : expression SUM expression')

    def p_expression_minus(self, p):
        'expression : expression SUB expression'
        p[0] = p[1] + p[2] + p[3]
        print('expression : expression SUB expression')

    def p_expression_and(self, p):
        'expression : expression AND expression'
        p[0] = p[1] + p[2] + p[3]
        print('expression : expression AND expression')

    def p_expression_or(self, p):
        'expression : expression OR expression'
        p[0] = p[1] + p[2] + p[3]
        print('expression : expression OR expression')

    # def p_expression_term(self, p):
    #     'expression : term'
    #     p[0] = p[1]
    #     print('expression : term')

    def p_term_times(self, p):
        'expression : expression MUL expression'
        p[0] = p[1] + p[2] + p[3]
        print('expression : expression MUL expression')

    def p_term_div(self, p):
        'expression : expression DIV expression'
        p[0] = p[1] + p[2] + p[3]
        print('expression : expression DIV expression')

    def p_term_MOD(self, p):
        'expression : expression MOD expression'
        p[0] = p[1] + p[2] + p[3]
        print('expression : expression MOD expression')

    def p_term_factor(self, p):
        'expression : factor'
        p[0] = p[1]
        print('expression : factor')

    def p_factor_num(self, p):
        'factor : INTEGERNUMBER'
        p[0] = str(p[1])
        print('factor : INTEGERNUMBER')

    def p_factor_float(self, p):
        'factor : FLOATNUMBER'
        p[0] = str(p[1])
        print('factor : FLOATNUMBER')

    def p_factor_true(self, p):
        'factor : TRUE'
        p[0] = p[1]
        print('factor : TRUE')

    def p_factor_false(self, p):
        'factor : FALSE'
        p[0] = p[1]
        print('factor : FALSE')

    def p_factor_expr(self, p):
        'factor : LRB expression RRB'
        p[0] = p[1] + p[2] + p[3]
        print('factor : LRB expression RRB')



    precedence = (
        ('left', 'SHIFT_IF'),
        ('left', 'SHIFT_IFELSE'),
        ('left', 'SHIFT_ELSEIFLIST'),
        # ('left', 'SHIFT_ELSEIF'),
        # ('left', 'SHIFT_VARDEC'),
        ('left', 'SHIFT_LVALUE'),
        ('left', 'SHIFT_IDDEC'),
        ('left', 'SHIFT_ASSIGN'),
        ('left', 'IF'),
        ('left', 'ELSE'),
        ('left', 'ELSEIF'),
        ('left', 'COMMA'),
        ('right', 'ASSIGN'),
        ('left', 'OR'),
        ('left', 'AND'),
        ('left', 'EQ', 'NE'),
        ('left', 'GT', 'LT', 'GE', 'LE'),
        ('left', 'SUM', 'SUB'),
        ('left', 'MUL', 'DIV', 'MOD'),
        ('right', 'NOT'),
    )


    # Error rule for syntax errors
    def p_error(self, p):
        if p is not None:
            print("\t[Error]Syntax error in input! ", p.value )
        else:
            print("\t[Error]Syntax error in input! ")

    def build(self, **kwargs):
        self.parser = yacc.yacc(module=self, **kwargs)
        return self.parser

    # ===============================================================


