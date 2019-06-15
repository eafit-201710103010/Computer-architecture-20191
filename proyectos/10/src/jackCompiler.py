import sys
from antlr4 import *
import os
from jackGrammarParser import jackGrammarParser
from jackListener import jackListener
from jackGrammarLexer import jackGrammarLexer
from jackErrorListener import jackErrorListener

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

    for jackFile in dirs:
        """Por cada file creo los elementos necesarios para su procesamiento"""
        imput = FileStream(jackFile)
        lexer = jackGrammarLexer(imput)
        stream = CommonTokenStream(lexer) 
        parser = jackGrammarParser(stream) 
        parser.removeErrorListeners()
        errorListener = jackErrorListener()
        parser.addErrorListener(errorListener)
        
        try: 
            tree = parser.classNT()
            listener = jackListener(parser,jackFile)    
            ParseTreeWalker.DEFAULT.walk(listener,tree)         
        except Exception as e: 
           print(e) 
           exit(1)   
        del lexer,stream,parser,listener,tree