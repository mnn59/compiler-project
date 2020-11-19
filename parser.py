from lexer import Lexer
import ply.yacc as yacc


class Parser:

    tokens = Lexer().tokens

    def __init__(self):
        pass

        # Yacc example

    def p_expression_plus(self, p):
        'expression : expression PLUS term'
        p[0] = p[1] + p[3]

    def p_expression_minus(self, p):
        'expression : expression MINUS term'
        p[0] = p[1] - p[3]

    def p_expression_term(self, p):
        'expression : term'
        p[0] = p[1]

    def p_term_times(self, p):
        'term : term TIMES factor'
        p[0] = p[1] * p[3]

    def p_term_div(self, p):
        'term : term DIVIDE factor'
        p[0] = p[1] / p[3]

    def p_term_factor(self, p):
        'term : factor'
        p[0] = p[1]

    def p_factor_num(self, p):
        'factor : NUMBER'
        p[0] = p[1]

    def p_factor_expr(self, p):
        'factor : LPAREN expression RPAREN'
        p[0] = p[2]

    # Error rule for syntax errors
    def p_error(self, p):
        print("Syntax error in input!")

    def build(self, **kwargs):
        self.parser = yacc.yacc(module=self, **kwargs)
        return self.parser