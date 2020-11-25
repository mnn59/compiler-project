from lexer import Lexer
import ply.yacc as yacc


class Parser:

    tokens = Lexer().tokens

    def __init__(self):
        pass

        # Yacc example

    def p_program(self, p):
        'program : expression'

        print('program : expression')

    # def p_program_rel(self, p):
    #     'expression : relopexp'
    #     print('expression : relopexp')

    def p_expression_plus(self, p):
        'expression : expression SUM term'
        p[0] = p[1] + p[3]
        print('expression : expression SUM term')

    def p_expression_minus(self, p):
        'expression : expression SUB term'
        p[0] = p[1] - p[3]
        print('expression : expression SUB term')

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

    def p_term_factor(self, p):
        'term : factor'
        p[0] = p[1]
        print('term : factor')
    #
    def p_factor_num(self, p):
        'factor : INTEGERNUMBER'
        p[0] = p[1]
        print('factor : INTEGERNUMBER')

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

    # def p_relop_gt(self, p):
    #     'relopexp : relopexp GT expression'
    #     p[0] = p[1] > p[3]
    #     print('relopexp : relopexp GT expression')

    precedence = (
        ('left', 'EQ', 'NE', 'GE', 'LE', 'GT', 'LT'),
        ('left', 'SUM', 'SUB'),
        ('left', 'MUL', 'DIV'),
    )


    # Error rule for syntax errors
    def p_error(self, p):
        print("Syntax error in input! " + p.value )

    def build(self, **kwargs):
        self.parser = yacc.yacc(module=self, **kwargs)
        return self.parser