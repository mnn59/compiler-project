from lexer import Lexer

lexer = Lexer().build()
file = open('amirhaf76_test.txt')
text_input = file.read()
file.close()
lexer.input(text_input)
while True:
    tok = lexer.token()
    if not tok:  # EOF(end of file)
        break
    print(tok)
