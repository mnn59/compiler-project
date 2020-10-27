from ply import lex
from ply.lex import TOKEN


class Lexer:
    # LRB: ( , RRB: ) , LCB: { , RCB: } , LT: < , GT: >
    tokens = [
        'IF', 'WHILE', 'PRINT',
        'LRB', 'RRB', 'LCB', 'RCB',
        'INTEGER', 'SUM', 'SUB', 'MUL', 'DIV',
        'LT', 'GT', 'SEMICOLON'
    ]

    # COLONS
    t_SEMICOLON = r'\;'
    # BRACKETS
    t_LRB = r'\('
    t_RRB = r'\)'
    t_LCB = r'\{'
    t_RCB = r'\}'
    # OPERATOR
    t_SUM = r'\+'
    t_SUB = r'\-'
    t_MUL = r'\*'
    t_DIV = r'\/'
    t_LT = r'\<'
    t_GT = r'\>'
    # RESERVED KEYWORD
    t_IF = r'if'
    t_WHILE = r'while'
    t_PRINT = r'print'

    # digit = r'([1-9])'
    # zero = r'([0])'
    # var = r'(' + digit + r'(' + digit + r'|' + zero + r')*)'
    #
    # @TOKEN(var)
    def t_INTEGER(self, t):
        # for me
        # r"""[+|-]?[1-9]([1-9]|[0])*"""
        # t.value = int(t.value)

        r"""[0-9]+"""
        t.value = int(t.value)

        # r"""[0-9]{1,9}"""
        # t.value = int(t.value)

        # r'((?!^0\d+)^0)|((?!0+)\d{1,10})'
        # r'\#[-\+]?([1-9]\d*|0)'      # for robati

        # r'[-|+]?(\d+)'
        return t

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # characters that we want from lexer to skip theme
    # NOTE: it must be lower case 'ignore' not 'IGNORE'
    t_ignore = '\n \t'

    # NOTE: t.value = lexeme  t.type = token
    # NOTE: it must be lower case 'error' not 'ERROR'
    def t_error(self, t):
        raise Exception('Error at ', t.value)

    def build(self, **kwargs):
        self.lexer = lex.lex(self, **kwargs)
        return self.lexer

# issues:
# 1. 002 --> 2
# 2. 2+3 --> 2 + 3
