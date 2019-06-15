from jackGrammarVisitor import  jackGrammarVisitor
from symbol_table import SymbolTable
from code_writer import CodeWriter

class jackVisitor(jackGrammarVisitor):
    """Clase que hereda del visitor para ir escribiendo en lenguaje de maquina virtual"""

    def __init__(self):
        """Inciializa una tabald e simbolos y un ecritor de codigo junto con variables auxiliares"""
        self.symbolTable = SymbolTable()
        self.contWhile = -1
        self.contIf = -1
        self.nombreClase = ""
        self.kindMetodo = ""
        self.nombreMetodo = ""
        self.vmWriter = CodeWriter()
        self.vmWriter.vm = ""
        self.nArgs = 0

    def visitClasses(self, ctx):
        """Obtiene y guarda el nombre de la clase actualmente compilada"""
        self.nombreClase = ctx.children[1].children[0].getText()
        return self.visitChildren(ctx)

    def visitClassVarDec(self, ctx):
        """Guarda en la tabla de simbolos cada uno de los fields  variables taticas declaradas """
        kind = ctx.children[0].getText()
        tipo = ctx.children[1].children[0].getText()
        i = 2
        while ctx.children[i].getText() != ';': 
            name = ctx.children[i].getText()  
            if name == ',':
                pass
            else:
                self.symbolTable.define(name, tipo, kind)
            i +=1
        return self.visitChildren(ctx)

    def visitTypes(self, ctx):
        return self.visitChildren(ctx)

    def visitSubroutineDec(self, ctx):
        """Inicializa en la tabla de simbolos una subrotina, y en caso de se un metodo agrega this como parametro"""
        self.kindMetodo = ctx.children[0].getText()
        self.nombreMetodo = ctx.children[2].children[0].getText()
        self.symbolTable.startSubroutine()
        if self.kindMetodo == 'method':
            self.symbolTable.define('this', self.nombreMetodo, 'argument')
        return self.visitChildren(ctx)

    def visitParameterList(self, ctx):
        """Agrega a la tabla de simbolos de la subroutina cada uno de los parametros """
        if ctx.getChildCount() > 0:
            tipo = ctx.children[0].children[0].getText()
            nombre = ctx.children[1].children[0].getText()
            self.symbolTable.define(nombre, tipo, 'argument')
            i = 2
            while i < len(ctx.children)-1  and ctx.children[i].getText() != ')':
                tipo = ctx.children[i+1].getText()
                nombre = ctx.children[i+2].getText()
                self.symbolTable.define(nombre, tipo, 'argument')
                i+=3
        return self.visitChildren(ctx)

    def visitSubroutineBody(self, ctx):
        """Despues de contar las variables locales escribe la funcion en 
        maquina virtual y dependiendo del tipo de funcion hace los llamados, push y pop correspondientes"""
        i = 1
        while ctx.children[i].children[0].getText() == "var":
            self.visit(ctx.children[i])
            i += 1
        funcion = self.nombreClase +'.'+ self.nombreMetodo
        numLcl = self.symbolTable.varCount('local')
        self.vmWriter.writeFunction(funcion, numLcl)
        if self.kindMetodo == 'constructor':
            numFields = self.symbolTable.varCount('field')
            self.vmWriter.writePush('constant', numFields)
            self.vmWriter.writeCall('Memory.alloc', 1)
            self.vmWriter.writePop('pointer', 0)
        elif self.kindMetodo == 'method':
            self.vmWriter.writePush('argument', 0)
            self.vmWriter.writePop('pointer', 0)
        while i < ctx.getChildCount():
            self.visit(ctx.children[i])
            i += 1

    def visitVarDec(self, ctx):
        """Inicializa en la tabla de simbolos todas las variables locales de la subrutina para poder escribir la función"""
        tipo = ctx.children[1].children[0].getText()
        nombre = ctx.children[2].getText()
        self.symbolTable.define(nombre, tipo, 'local')
        i = 3
        while ctx.children[i].getText() != ';':
            nombre = ctx.children[i].getText()
            if nombre == ',':
                pass
            else:
                self.symbolTable.define(nombre, tipo, 'local')
            i += 1
        return self.visitChildren(ctx)

    """Llamados en los que no es necesario  escribir codigo de VM"""
    def visitClassName(self, ctx):
        return self.visitChildren(ctx)

    def visitSubroutineName(self, ctx):
        return self.visitChildren(ctx)

    def visitVarName(self, ctx):
        return self.visitChildren(ctx)

    def visitStatements(self, ctx):
        return self.visitChildren(ctx)

    def visitStatement(self, ctx):
        return self.visitChildren(ctx)

    def visitLetStatement(self, ctx): 
        """Realiza los push y pop necesarios para guardar un valor y asignarle una posiicon en memoria"""
        nombre = ctx.children[1].getText()
        tipo = self.symbolTable.kindOf(nombre)
        index = self.symbolTable.indexOf(nombre)
        if tipo  == None:
            tipo = self.symbolTable.kindOf(nombre)
            index = self.symbolTable.indexOf(nombre)
        if ctx.children[2].getText() == '[':
            self.visit(ctx.children[3])
            self.vmWriter.writePush(tipo,index)
            self.vmWriter.writeArithmetic('add')
            self.visit(ctx.children[6]) 
            self.vmWriter.writePop('temp', 0)           
            self.vmWriter.writePop('pointer', 1)
            self.vmWriter.writePush('temp', 0)
            self.vmWriter.writePop('that', 0)
        else:
            self.visit(ctx.children[3])
            self.vmWriter.writePop(tipo,index)

    def visitIfStatement(self, ctx):
        """Escribe los labels necesarios para manejar el flujo del programa de a cuerdo a lo indicado por la expresión"""
        self.contIf += 1
        cont = self.contIf
        self.visit(ctx.children[2])
        self.vmWriter.writeIf('IF_TRUE' + str(cont))
        self.vmWriter.writeGoto('IF_FALSE' + str(cont))
        self.vmWriter.writeLabel('IF_TRUE' + str(cont))
        self.visit(ctx.children[5])
        if ctx.getChildCount() > 7 :
            if str(ctx.children[7]) == 'else':
                self.vmWriter.writeGoto('IF_END' + str(cont))
                self.vmWriter.writeLabel('IF_FALSE' + str(cont))
                self.visit(ctx.children[9])
                self.vmWriter.writeLabel('IF_END' + str(cont))
        else:
            self.vmWriter.writeLabel('IF_FALSE' + str(cont))

    def visitWhileStatement(self, ctx):
        """Similar al if, escribe labels para que el flujo del programa se repita hasta que una condicion no se cumpla"""
        self.contWhile += 1 
        contW = self.contWhile
        self.vmWriter.writeLabel('WHILE_EXP' + str(contW))
        self.visit(ctx.children[2])
        self.vmWriter.writeArithmetic('not')
        self.vmWriter.writeIf('WHILE_END' + str(contW))
        self.visit(ctx.children[5])
        self.vmWriter.writeGoto('WHILE_EXP' + str(contW))
        self.vmWriter.writeLabel('WHILE_END' + str(contW))

    def visitDoStatement(self, ctx):
        """Hago el llamado y posteriormente vuelvo a la función de donde hice el llamado"""
        self.visitChildren(ctx)
        self.vmWriter.writePop('temp', 0)

    def visitReturnStatement(self, ctx):
        """Obtengo valor de retorno, si no hay, el valor de retorno es 0"""
        if ctx.children[1].getText() != ';':
            self.visit(ctx.children[1])
        else:
            self.vmWriter.writePush('constant', 0)
        self.vmWriter.writeReturn()

    def visitExpression(self, ctx):
        """Separo al expresion por partes para irla compilando"""
        self.visit(ctx.children[0])
        i = 2
        while i < ctx.getChildCount():
            self.visit(ctx.children[i])
            self.visit(ctx.children[i-1])
            i +=2

    def visitTerm(self, ctx):
        """Determino el tipo de termino,si es un tipo de dato o un valor de un arreglo, dependiendo de esto obtengo 
        su valor si está en la tabla de simbolos o lo busco en un arreglo o busco el siguiente etrmino con el que opera y lo guardo en memoria"""
        term = ctx.children[0].getText()
        if ctx.getChildCount() == 1:
            if term.isdigit():
                self.vmWriter.writePush('constant', term)
            elif term.startswith('"'):
                term = term.strip('"')
                tam = len(term)
                self.vmWriter.writePush('constant', tam)
                self.vmWriter.writeCall('String.new', 1)
                for char in term:
                    self.vmWriter.writePush('constant', ord(char))
                    self.vmWriter.writeCall('String.appendChar', 2)
            elif term in ['true', 'false', 'null', 'this']:
                self.visitChildren(ctx)
            elif term in self.symbolTable.subrutina.keys():
                tipo = self.symbolTable.kindOf(term)
                index = self.symbolTable.indexOf(term)
                self.vmWriter.writePush(tipo,index)
            elif term in self.symbolTable.clase.keys():
                tipo = self.symbolTable.kindOf(term)
                index = self.symbolTable.indexOf(term)
                self.vmWriter.writePush(tipo,index)
            else:
                self.visitChildren(ctx) 
        else:
            var = ctx.children[0].getText()
            if ctx.children[1].getText() == '[':
                index = self.symbolTable.indexOf(var)
                segment = self.symbolTable.kindOf(var)
                self.visit(ctx.children[2])
                self.vmWriter.writePush(segment, index)
                self.vmWriter.writeArithmetic('add')
                self.vmWriter.writePop('pointer', '1')
                self.vmWriter.writePush('that', '0')
            elif term == '(':
                self.visitChildren(ctx)
            elif term  == '-':
                self.visit(ctx.children[1])
                self.visit(ctx.children[0])
            elif term  == '~':
                self.visit(ctx.children[1])
                self.visit(ctx.children[0])

    def visitSubroutineCall(self, ctx):
        """Ubica la subrutina de acuerdo a la clase en la que se encuentre y escribe en VM el respectivo llamado con su paso de parametros"""
        nombre = ctx.children[0].children[0].getText()
        funcion = nombre
        args = 0
        if ctx.children[1].getText() == '.':    
            nombreSubrutina = ctx.children[2].children[0].getText()
            tipo = self.symbolTable.typeOf(nombre)
            if tipo != None:
                kind = self.symbolTable.kindOf(nombre)
                index = self.symbolTable.indexOf(nombre)
                self.vmWriter.writePush(kind, index)
                funcion = tipo + '.' + nombreSubrutina
                args += 1
            else: 
                funcion = nombre + '.' + nombreSubrutina
        elif ctx.children[1].getText() == '(':
            funcion =  self.nombreClase + '.' + nombre
            args += 1
            self.vmWriter.writePush('pointer', 0)
        self.visitChildren(ctx)
        args = args +self.nArgs
        self.vmWriter.writeCall(funcion, args)

    def visitExpressionList(self, ctx):
        """Evalua cada expresion indivudualmente"""
        self.nArgs = 0
        if ctx.getChildCount() > 0:
            self.nArgs = 1
            self.visit(ctx.children[0])
            i = 2
            while i < ctx.getChildCount():
                self.visit(ctx.children[i])
                self.visit(ctx.children[i-1])
                self.nArgs += 1
                i += 2

    def visitOp(self, ctx):
        """Genera el comando de VM respectivo dependiendo del operador"""
        op = ctx.children[0].getText()
        if op == "+":
            self.vmWriter.writeArithmetic('add')
        elif op == "-":
            self.vmWriter.writeArithmetic('sub')
        elif op == "*":
            self.vmWriter.writeArithmetic('call Math.multiply 2')
        elif op == "/":
            self.vmWriter.writeArithmetic('call Math.divide 2')
        elif op == "&":
            self.vmWriter.writeArithmetic('and')
        elif op == "|":
            self.vmWriter.writeArithmetic('or')
        elif op == ">":
            self.vmWriter.writeArithmetic('gt')
        elif op == "<":
            self.vmWriter.writeArithmetic('lt')
        elif op == "=":
            self.vmWriter.writeArithmetic('eq')
        return self.visitChildren(ctx)

    def visitUnaryop(self, ctx):
        """Determina el comando de VM para cada operaodr unario"""
        op = ctx.children[0].getText()
        if op == "~":
            self.vmWriter.writeArithmetic('not')
        elif op == "-":
            self.vmWriter.writeArithmetic('neg')

    def visitKeywordconstant(self, ctx):
        """Escribe el comando de VM para poder hacer uso de una palabra reservada espcifica"""
        keyword = ctx.children[0].getText()
        if keyword == 'this':
            self.vmWriter.writePush('pointer', 0)
        elif keyword in ['false','null']:
            self.vmWriter.writePush('constant', 0)
        elif keyword == 'true':
            self.vmWriter.writePush('constant', 0)
            self.vmWriter.writeArithmetic('not')
        return self.visitChildren(ctx)

    def crearArchivo(self,path):
        """Abre el archivo .vm donde se escribirán lso comandos de máquina virtual"""
        filewrite = path.split('.jack') #Reemplazo el .jack con .xml si lo tiene 
        filewritef = filewrite[0]+'.vm'  #Sino le agrego el .
        codigoVM = self.vmWriter.vm
        archivo = filewritef
        try:
            file = open(archivo,'w')  #Abro el file en modo escribir
        except FileNotFoundError:
            print('ERROR:No hay directorio existente para escribir')   
            exit(1) 
        file.write(codigoVM)


