import sys
from antlr4 import CommonTokenStream, ParseTreeWalker, FileStream

from MiniPythonLexer import MiniPythonLexer
from MiniPythonParser import MiniPythonParser


def analizar(archivo):
    print(f"\n=== Analizando {archivo} ===", flush=True)
    input_stream = FileStream(archivo)
    lexer = MiniPythonLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MiniPythonParser(stream)
    
    sys.stdout.flush()
    tree = parser.program()
    sys.stderr.flush()
    
    if parser.getNumberOfSyntaxErrors() == 0:
        print("Resultado: El análisis terminó OK.", flush=True)
    else:
        print(f"Resultado: El análisis terminó con errores. (Total: {parser.getNumberOfSyntaxErrors()})", flush=True)



print('Comenzando...')

analizar('residuos.sem')
analizar('incorrecto.sem')
analizar('incorrecto2.sem')

print('\nFin.')

