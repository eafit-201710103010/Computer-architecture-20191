from jackGrammarListener import jackGrammarListener
from jackGrammarParser import jackGrammarParser
"""Clase que hereda de listener para generar xml"""
class jackListener(jackGrammarListener):

    KEYWORDS=['class','constructor','function','method','field','static','var','int','char','boolean','void','true','false','null','this','let','do','if','else','while','return']
    SYMBOLS=['{','}','(',')','.',',',';','+','-','*','/','&','|','>','<','=','~','[',']']
    NON_TERMINALS=['classNT','classVarDec','subroutineDec','parameterList','subroutineBody','varDec','statements','whileStatement','ifStatement','returnStatement','letStatement','doStatement','expression','term','expressionList']
    
    def __init__(self,parser,outname):
        filewrite = outname.split('.jack') #Reemplazo el .jack con .xml si lo tiene 
        filewritef = filewrite[0]+'.xml'  #Sino le agrego el .xml
        try:
            self.outname = open(filewritef, 'w')    #Abro el file en modo escribir
        except FileNotFoundError:
            print('ERROR:No hay directorio existente para escribir')   
            exit(1) 
        self.file=outname.split('.jack')[0].split("/")[-1]   #Nombre del file que estoy analizando
        if '\\' in self.file:                               
            self.file=self.file.split('\\')[-1]
        self.parser=parser
        self.indent =" "
        self.indentLevel = 0

    def enterEveryRule(self,ctx):  
        """Al entrar a cada regla escribir el tag de apertura"""
        #Obtengo al regale en la que estoy
        rule = self.parser.ruleNames[ctx.getRuleIndex()]
        #Miro si si se escribe en el xml
        if rule in jackListener.NON_TERMINALS:
            if rule=='classNT':
                rule='class'  
            tag="{}<{}>\n".format(self.calcularIndent(),rule)
                #La escribo
            self.outname.write(tag) 
            self.indentLevel+=1  
        return super().enterEveryRule(ctx)

    def exitEveryRule(self,ctx):
        """Al salir de cada regla escribir el tag de cierre"""
        #Obtengo al regale en la que estoy
        rule = self.parser.ruleNames[ctx.getRuleIndex()]
        #Miro si si se escribe en el xml
        if rule in jackListener.NON_TERMINALS:
            if rule=='classNT':
                rule='class'   
            self.indentLevel-=1
            #La escribo
            tag="{}</{}>\n".format(self.calcularIndent(),rule)
            self.outname.write(tag)    
        return super().exitEveryRule(ctx)

    def visitTerminal(self,node):
        """Escribo el terminal dentro de los tags"""
        terminal_value = node.getText()
        #Busco el tipo de terminal
        typet = self.get_token_group(terminal_value.strip())
        cont=''
        if typet=='stringConstant' :
            #Si es string quito comillas
            cont=terminal_value[1:-1]
        elif typet=='identifier' or typet=='keyword':
            cont=terminal_value
        elif typet=='integerConstant':
            #Paso  entero y evaluo que esté dentro del rango
            cont=int(terminal_value)
            if cont<0 or cont>32767:
                print('ERROR: Integer out of range')
                exit(1)
        else:     
            #Hago los respectivos cambios si es un símbolo
            if terminal_value=='<':
                cont='&lt;'
            elif terminal_value=='>':
                cont='&gt;'    
            elif terminal_value=='&':
                cont='&amp;'   
            elif terminal_value=='"':
                cont='&quot;'  
            else:
                cont =terminal_value.strip()        
        #Escribo en el archivo
        self.outname.write("{0}<{2}>{1}</{2}>\n".format(self.calcularIndent(),cont,typet))
        return super().visitTerminal(node)

    def calcularIndent(self):
        return self.indentLevel*self.indent

    def get_token_group(self,terminal):
        """Metodo que determina el tipo de terminal"""
        if terminal.isdigit():
            return 'integerConstant'
        elif terminal in jackListener.KEYWORDS:
            return 'keyword'    
        elif '"' in terminal:
            return 'stringConstant'
        elif terminal.isalnum():
            return 'identifier'    
        elif terminal in jackListener.SYMBOLS:
            return 'symbol'   


