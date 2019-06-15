class Parser:
    def __init__(self,dir):
        try:
            self.f = open(dir)                                             #Trato de abrir el archivo 
        except (PermissionError, FileNotFoundError):
            print("ERROR: No se puede acceder al archivo especificado "+dir)
            exit(1)  
        self.listLines = self.f.readlines()                                #Obtengo todas las lineas
        self.listLines = [x for x in self.listLines if len(x.strip())!=0]  #Ignoro las lineas vacias
        self.currentCommand = None
        self.thisCommandType=None
        self.countLine = -1

    def hasMoreCommands(self):
        if self.countLine < (len(self.listLines)-1) : #Si aun quedan lineas por leer retornar True
            return True
        else:
            return False

    def advance(self):
        while self.hasMoreCommands():
            self.countLine +=1
            self.currentCommand = self.listLines[self.countLine]    #Obtengo nueva linea
            self.currentCommand = self.quitar_comentario()          #Quito los comentarios que tenga
            if len(self.currentCommand.strip()) != 0 :              #Si quedo linea vacia avanzo de nuevo
                break   
            

    def commandType(self):
        arit = ['add', 'sub', 'neg', 'eq', 'gt', 'lt', 'and', 'or', 'not']  #Comandos aritmeticos
        if 'push' in self.currentCommand:
            self.thisCommandType= 'C_PUSH'
            return 'C_PUSH'
        elif 'pop' in self.currentCommand:
            self.thisCommandType= 'C_POP'
            return 'C_POP'
        elif 'label' in self.currentCommand.strip().split(' ')[0]:  #Para que un label se pueda llamar label
            self.thisCommandType= 'C_LABEL'
            return 'C_LABEL'
        elif 'if-goto' in self.currentCommand:
            self.thisCommandType= 'C_IF'
            return 'C_IF'
        elif 'return' in self.currentCommand:
            self.thisCommandType= 'C_RETURN'
            return 'C_RETURN'
        elif 'call' in self.currentCommand:
            self.thisCommandType= 'C_CALL'
            return 'C_CALL'
        elif self.currentCommand.strip() in arit:   #Si esta en la lista definida de aritmeticos
            self.thisCommandType= 'C_ARITHMETIC'
            return 'C_ARITHMETIC'
        elif 'goto' in self.currentCommand:
            self.thisCommandType=  'C_GOTO' 
            return 'C_GOTO' 
        elif 'function' in self.currentCommand:
            self.thisCommandType= 'C_FUNCTION' 
            return 'C_FUNCTION'        
        else:
            print("ERROR: El comando "+self.currentCommand.strip() +
                  " no pertenece al lenguaje de máquina virtual")
            exit(1)

    def quitar_comentario(self):
        if "//" in self.currentCommand:
            arr = self.currentCommand.split("//")
            return arr[0]
        else:
            return self.currentCommand

    def arg1(self):
        partes = self.currentCommand.strip().split(' ')
        if(len(partes)==1):               #Si es solo una palabra es porque es aritmetico o return
            return self.currentCommand    #Retorno todo
        else:
            return partes[1]              #Retorno la segunda parte
          

    def arg2(self):
        partes = self.currentCommand.strip().split(' ')
        arg3 = ['C_PUSH','C_POP','C_FUNCTION','C_CALL']                 #Comandos que necesitan de arg2
        if(len(partes)==3 and self.thisCommandType in arg3):            #Para arg2 deben haber al menos 3 partes
            return partes[-1].strip()                                   #Retorno el ultimo
        else:
            print("ERROR: Pocos o demasiados argumentos en el comando "+self.currentCommand.strip() )
            exit(1)