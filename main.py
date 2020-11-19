from lexer import Lexer
from parser import Parser

lexer = Lexer().build()
file = open('test.txt')
text_input = file.read()
file.close()
lexer.input(text_input)
# while True:
#     tok = lexer.token()
#     if not tok:  # EOF(end of file)
#         break
#     print(tok)
# p = Parser()
# p.build().parse(text_input, lexer, False)

