from ply import lex
from ply.lex import TOKEN


class Lexer:
    # LRB: ( , RRB: ) , LCB: { , RCB: } , LT: < , GT: >
    # amir.haf76: there is DOT token
    tokens = [
        'ID', 'INTEGERNUMBER', 'FLOATNUMBER', 'INTEGER', 'FLOAT',
        'BOOLEAN', 'FUNCTION', 'TRUE', 'FALSE', 'PRINT', 'RETURN',
        'MAIN', 'IF', 'ELSE', 'ELSEIF', 'WHILE', 'ON', 'WHERE',
        'FOR', 'AND', 'OR', 'NOT', 'IN', 'ASSIGN',
        'SUM', 'SUB', 'MUL', 'DIV', 'MOD',
        'GT', 'GE', 'LT', 'LE', 'EQ', 'NE',
        'LCB', 'RCB', 'LRB', 'RRB', 'LSB', 'RSB',
        'SEMICOLON', 'COLON', 'COMMA', 'ERROR', 'DOT'
    ]

    reserved = {
        # TYPES
        'int': "INTEGER",
        'float': "FLOAT",
        'bool': "BOOLEAN",
        # LOOPS
        'while': "WHILE",
        'for': "FOR",
        # CONDITIONAL
        'if': "IF",
        'else': "ELSE",
        'elseif': "ELSEIF",
        # BOOLEAN
        'True': "TRUE",
        'False': "FALSE",
        # COMPARISON
        'and': "AND",
        'or': "OR",
        'not': "NOT",
        # Other
        'print': "PRINT",
        'return': "RETURN",
        'main': "MAIN",
        # 'Function': "Function",
        'fun': "FUNCTION",
        'on': "ON",
        'in': "IN",
        'where': "WHERE",
    }

    # Todo literals
    # Todo newline
    # Todo eof  The lexpos attribute is reset so be aware of that if you're using it in error reporting.
    # Todo the order of definition of tokens should be edited

    # COLONS
    # t_SEMICOLON = r'\;'
    # t_COLON = r'\:'
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
    # t_LT = r'\<'
    # t_GT = r'\>'

    # RESERVED KEYWORD
    t_IF = r'if'
    t_WHILE = r'while'
    t_PRINT = r'print'

    # amir.haf76: start defining new tokens
    t_EQ = r'\=\='
    t_GE = r'\>='
    t_LE = r'\<='
    t_ASSIGN = r'\='
    t_NE = r'\!\='
    t_GT = r'\>'
    t_LT = r'\<'

    # COLONS
    t_SEMICOLON = r'\;'
    t_COLON = r'\:'
    t_COMMA = r'\,'
    # amir.haf76: there is extra token. it's '.'
    t_DOT = r'\.'

    # t_FUNCTION = r'fun'

    literals = ['{', '}', '(', ')', '[', ']',
                '*', '/', '%', '+', '-']

    # amir.haf76: end defining new tokens

    # amir.haf76: adding float number, float number should be upper than integer number!!!
    def t_FLOATNUMBER(self, t):
        r'(?<!\d)\+?\-?\d+\.\d+'
        t.value = float(t.value)
        return t

    def t_INTEGERNUMBER(self, t):
        r'[0-9]{1,9}'
        t.value = int(t.value)
        return t

    # digit = r'([1-9])'
    # zero = r'([0])'
    # var = r'(' + digit + r'(' + digit + r'|' + zero + r')*)'
    #
    # @TOKEN(var)
    # it can be commented
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

    def t_ID(self, t):
        r'[a-z_][a-zA-Z0-9_]*'
        if t.value in self.reserved:
            t.type = self.reserved[t.value]
        return t

    # Define a rule so we can track line numbers
    def t_newline(self, t):
        r'\n+'
        print(t.value)
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
