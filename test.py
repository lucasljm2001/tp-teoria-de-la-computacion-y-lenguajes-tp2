from antlr4 import CommonTokenStream, ParseTreeWalker, FileStream

from MiniPythonLexer import MiniPythonLexer
from MiniPythonParser import MiniPythonParser



print('Comenzando...')
input = FileStream('residuos.sem')
lexer = MiniPythonLexer(input)
stream = CommonTokenStream(lexer)
parser = MiniPythonParser(stream)

tree = parser.program()


print('Fin.')
