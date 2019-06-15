class CodeWriter:
    """Clase que almacena en una variable string lo que irá en al archivo .vm
    Basicamente cada clase recibe como parámetro los valores que irán en el 
    comando y les agrega la palabra reservada correspondiente"""
    vm = ""

    def __init__(self):
        self.vm = ""

    def writePush(self,segment,index):
        self.vm += "push " + segment + " " + str(index) + "\n"

    def writePop(self,segment,index):
        self.vm += "pop " + segment + " " + str(index) +"\n"

    def writeArithmetic(self,command):
        self.vm += command + "\n"

    def writeLabel(self,name):
        self.vm += "label " + name + "\n"

    def  writeGoto(self,name):
        self.vm += "goto " + name + "\n"

    def writeIf(self,name):
        self.vm += "if-goto " + name + "\n"

    def writeCall(self,name, nArgs):
        self.vm += "call " + name + " " + str(nArgs) + "\n"

    def writeFunction(self,name,nLocals):
        self.vm += "function " + name + " " + str(nLocals) + "\n"

    def writeReturn(self):
        self.vm += "return\n"