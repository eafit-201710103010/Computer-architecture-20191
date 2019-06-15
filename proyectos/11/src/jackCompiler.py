from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker, TerminalNode
from antlr4.error.ErrorListener import ErrorListener
from jackGrammarLexer import jackGrammarLexer
from jackGrammarListener import jackGrammarListener
from jackGrammarParser import jackGrammarParser
from jackVisitor import jackVisitor
import sys,os,glob

class Errors(ErrorListener):
    """Clase que escribe en pantalla los errores generados"""
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print('ERROR: Syntax error in line {} and column {} by token {}'.format(line,column,offendingSymbol.text))
        sys.exit()

"""ejecucion principal del programa"""
#Miro que tengo los argumentos necesarios
if (len(sys.argv) < 2) :
    print("ERROR: Falta de argumentos")
    exit(1)
else:
    #Miro si es directorio o archivo individual
    if len(sys.argv)==2 and '.jack' not in sys.argv[1]:
        if sys.argv[1][-1] != '/':
            sys.argv[1]=sys.argv[1]+'/'  #Le pongo el ultimo slash si no lo tiene
        outname= sys.argv[1][:-1]+'/'+sys.argv[1].split('/')[-2]
        dirs = []
        for r, d, f in os.walk(sys.argv[1]):  #Hago uan lista con los .jack del directorio
            
            for file in f:
                if '.jack' in file:
                    dirs.append(os.path.join(r, file))    
    else:
        dirs=sys.argv
        del dirs[0]
        outname=dirs[0].split('.jack')[0]

    for archivo in dirs:
        #Creo los objetos necesarios para ejecutar el compilador
        stream = FileStream(archivo)
        lexer = jackGrammarLexer(stream)
        tokens = CommonTokenStream(lexer)
        parser = jackGrammarParser(tokens) 
        parser._listeners = [ Errors() ]
        tree = parser.classes()
        visitor = jackVisitor()
        visitor.visit(tree)
        visitor.crearArchivo(archivo)
        