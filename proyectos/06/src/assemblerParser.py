class Parser:
    def __init__(self, dir):
        try:            
            self.f=open(dir)            
        except (PermissionError,FileNotFoundError) as e: 
            print("ERROR: No se puede acceder al archivo especificado")   
            exit(1)
        self.listLines = self.f.readlines()
        self.currentCommand = None
        self.countLine=-1
    

    def hasMoreCommands(self):
        if self.countLine< (len(self.listLines)-1):
            return True
        else:
            return False    


    def advance(self):
        while True:
            self.countLine+=1
            self.currentCommand = self.listLines[self.countLine]
            self.currentCommand= self.quitar_comentario()
            if len(self.currentCommand.strip()) != 0 :
                break;
          

    def commandType(self):
        if '@' in self.currentCommand:            
            return 'A_COMMAND'
        elif '=' in self.currentCommand or ';' in self.currentCommand:
            return 'C_COMMAND'
        elif '(' in self.currentCommand and ')' in self.currentCommand:
            return 'L_COMMAND'
        else:
            print("ERROR: El comando "+self.currentCommand.strip()+" no pertenece a la gramatica de Assembler")
            exit(1)
               

    def symbol(self):
        line = self.currentCommand.strip()
        var = ""
        pos = 1
        if len(line)<2 :
            linea=str(self.countLine)
            print("ERROR: No hay suficientes parametros para el comando A en la linea "+linea)
            exit(1)
        char2 = line[pos]
        if line[0]=="(":
            comandol=True
        while char2 !=")" and char2 !="\n":           
            var += char2
            pos += 1           
            if pos>=len(line): break    
            else: char2 = line[pos]   
        line=line.strip()        
        var=var.strip()        
        if len(var)==0 and comandol:
            linea=str(self.countLine)
            print("ERROR: Falta de argumentos para establecer etiqueta en la linea: "+linea)      
            exit(1)   
        if not var[0].isidentifier() and not var.isnumeric():
            print("ERROR: Simbolo en el comando "+self.currentCommand.strip()+" no es un identifiador")   
            exit(1)         
        return var.strip()

    def dest(self):
     if '=' in self.currentCommand:
         return self.currentCommand.split('=')[0]
     else:
         return ''
            
    def comp(self):
        line =self.currentCommand
        arr=""
        if "=" in line:
            arr=line.split("=")
            if ";" in arr[1]:
                arr1=arr[1].split(";")
                var = arr1[0].strip() 
                return var    
            else:
                res=arr[1].split(" ")
                var= res[0].strip() 
                return var     
        if ";" in line:
            arr=line.split(";")
            return arr[0].strip()

    def jump(self):
        if ";" in self.currentCommand:
            com=self.currentCommand.split(';')[-1]
            return com[0:3]
        else:
            return ''   

    def quitar_comentario(self):
        if "//" in self.currentCommand:
            arr = self.currentCommand.split("//") 
            return arr[0]    
        else:
            return self.currentCommand    
