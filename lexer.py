from ply import lex
from ply.lex import TOKEN


class Lexer:
    # LRB: ( , RRB: ) , LCB: { , RCB: } , LT: < , GT: >
    tokens = [
        'ID', 'INTEGERNUMBER', 'FLOATNUMBER', 'INTEGER', 'FLOAT',
        'BOOLEAN', 'FUNCTION', 'TRUE', 'FALSE', 'PRINT', 'RETURN',
        'MAIN', 'IF', 'ELSE', 'ELSEIF', 'WHILE', 'ON', 'WHERE',
        'FOR', 'AND', 'OR', 'NOT', 'IN', 'ASSIGN',
        'SUM', 'SUB', 'MUL', 'DIV', 'MOD',
        'GT', 'GE', 'LT', 'LE', 'EQ', 'NE',
        'LCB', 'RCB', 'LRB', 'RRB', 'LSB', 'RSB',
        'SEMICOLON', 'COLON', 'COMMA', 'ERROR'
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
        'fun': "FUNCTION",
        'on': "ON",
        'in': "IN",
        'where': "WHERE",
    }

    # Todo eof  The lexpos attribute is reset so be aware of that if you're using it in error reporting.
    # Todo the order of definition of tokens should be edited

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

    # COLONS, OPERATOR, BRACKETS
    t_SEMICOLON = r'\;'
    t_COLON = r'\:'
    t_COMMA = r'\,'

    literals = ['{', '}', '(', ')', '[', ']',
                '*', '/', '%', '+', '-']

    # amir.haf76: end defining new tokens

    # amir.haf76: adding float number, float number should be upper than integer number!!
    def t_FLOATNUMBER(self, t):
        r'(?<!\d|\w)[\+\-]?(?:0*[1-9]\d{0,8}|0+)\.\d+(?!\w|[.])'
        t.value = float(t.value)
        return t

    def t_INTEGERNUMBER(self, t):
        # r'[0-9]{1,9}'
        r'(?<!(?:\d|\w))[\+\-]?\d{1,9}(?!\w|[.])'
        t.value = int(t.value)
        return t

    def t_ID(self, t):
        r'[a-z_][a-zA-Z0-9_]*|True|False'

        if t.value in self.reserved:
            t.type = self.reserved[t.value]
        return t

    # Define a rule so we can track line numbers
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    # characters that we want from lexer to skip theme
    # NOTE: it must be lower case 'ignore' not 'IGNORE'
    # NOTE: Don't ignore \n, because it's used in t_newline for getting number of line
    t_ignore = ' \t'

    # NOTE: t.value = lexeme  t.type = token
    # NOTE: it must be lower case 'error' not 'ERROR'

    err_sign = r'(?:\*|\/|\+|\-|\%)(?:(?:\s+)?(?:\*|\/|\+|\-|\%))+'
    err_id = r'(?:[0-9]+)?[a-zA-Z_][a-zA-Z0-9_]*'
    # err_num = r'\.?(?:\d+\.)(?:\d+\.)+(?:\d+)?|(?:\d+\.)(?!\d+)|(?<!\d)(?:\.\d+)(?!\d+)'
    err_num = r'(?:\w+|\d+|\.)+'
    err_genr = err_sign + r'|' + err_num + r'|' + err_id
    @TOKEN(err_genr)
    def t_ERROR(self, t):

        return t

    # amir.haf76: I added this part for changing name
    def t_LCB(self, t):
        r'\{'
        t.type = 'LCB'
        return t

    def t_RCB(self, t):
        r'\}'
        t.type = 'RCB'
        return t

    def t_LRB(self, t):
        r'\('
        t.type = 'LRB'
        return t

    def t_RRB(self, t):
        r'\)'
        t.type = 'RRB'
        return t

    def t_LSB(self, t):
        r'\['
        t.type = 'LSB'
        return t

    def t_RSB(self, t):
        r'\]'
        t.type = 'RSB'
        return t

    def t_SUM(self, t):
        r'\+'
        t.type = 'SUM'
        return t

    def t_SUB(self, t):
        r'\-'
        t.type = 'SUB'
        return t

    def t_MUL(self, t):
        r'\*'
        t.type = 'MUL'
        return t

    def t_MOD(self, t):
        r'\%'
        t.type = 'MOD'
        return t

    def t_DIV(self, t):
        r'\/'
        t.type = 'DIV'
        return t

    def t_error(self, t):
        t.value = t.value[0]
        t.lexer.skip(1)
        return t

    def build(self, **kwargs):
        self.lexer = lex.lex(self, **kwargs)
        return self.lexer

# issues:
# 1. 002 --> 2
# 2. 2+3 --> 2 + 3
