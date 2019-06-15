class code_writer:
    def __init__(self, filename):
        filename = filename.split('.vm') #Reemplazo el .vm con .asm
        filename = filename[0]+'.asm'
        self.f = open(filename, 'w')  #Abro el file en modo escribir
        self.filename=filename.split('.asm')[0].split('/')[-1]   #Ignoro el .asm y los directorios   
        self.code = ''  #Variable dodne ire acumulando lo que voy a escribir
        self.bool_count = 0 #Variable para saber cuantos gt ly o eq he ehcho

    def setFileName(self, filename):  #Lo mismo del constructor
        filename = filename.split('.vm')
        filename = filename[0]+'.asm'
        self.filename=filename.split('.asm')[0].split('/')[-1]  
        self.f = open(filename, 'w')

    def writeArithmetic(self, command): 
      #Defino operadores unarios binarios y comparacioens booleanas  
      unary = {         
          "neg": '-',
          "not": '!'
      }
      binary = {
          "add": '+',
          "sub": '-',
          "and": '&',
          "or": '|'
      }
      jump = {
          "eq": 'JEQ',
          "gt": 'JGT',
          "lt": 'JLT'
      }
      command=command.strip() #Elimino lineas nuevas
      if command in binary:
          self.code += '@SP\n'     #Busco tope de la pila
          self.code += 'AM=M-1\n'  #Le resto 1 y voy a esa posicion
          self.code += 'D=M\n'     #Guardo el contenido en D
          self.code += 'A=A-1\n'   #Voy a la posicion anterior
          self.code = self.code+'M=M'+binary[command]+'D\n' #Aplico la operacion indicada con D
      elif command in unary:
          self.code += '@SP\n'     #Busco el tope de la pila
          self.code += 'A=M-1\n'   #Voy al elemento mas arriba
          self.code = self.code+'M='+unary[command]+'M\n' #Le aplico la operación unaria
      elif command in jump:
          self.code += '@SP\n'     #Busco el tope de la pila
          self.code += 'AM=M-1\n'  #Le resto uno y voy alla
          self.code += 'D=M\n'     #Guardo el elemento más arriba en D
          self.code += 'A=A-1\n'   #Voy a la posicion anterior
          self.code = self.code+'D=M-D\n' #Resto ambos valores
          self.code = self.code+'@BOOL'+str(self.bool_count)+'\n' #Defino un salto enumerado
          self.code = self.code+'D;'+jump[command]+'\n' #Salto según la condición
          self.code += '@SP\n'   #Si no salté voy al tome de la pila
          self.code += 'A=M-1\n' #Le resto 1
          self.code += 'M=0\n'   #Guardo False
          self.code = self.code+'@ENDBOOL'+str(self.bool_count)+'\n' #Voy al final de la condicion
          self.code += '0;JMP\n'  #Salto
          self.code = self.code+'(BOOL'+str(self.bool_count)+')\n' #Salto enumerado si se cumple la condicion
          self.code += '@SP\n'    #Voy al tope de la pila
          self.code += 'A=M-1\n'  #Le resto 1
          self.code += 'M=-1\n'   #Lo pongo en True
          self.code = self.code+'(ENDBOOL'+str(self.bool_count)+')\n' #Aquí termina el condicional
          self.bool_count = self.bool_count+1 #Sumo 1 al contador de comparaciones booleanas
      else:
            print("ERROR: El comando "+str(command) +
                  " no fue reconocido en comandos aritmeticos")
            exit(1)

      self.f.write(self.code) #Escribo todo en el archivo nuevo
      self.code = ''  #Vacio la var auxiliar

    def writePushPop(self, command, segment, index):
        self.hallarDestino(segment,index) #Pongo en A la dirección 
        if command == 'C_PUSH':    
            if segment == 'constant':
                self.code+='D=A\n'  #Guardo directamente el dato
            else:
                self.code+='D=M\n'  #Guardo dato de la direccion 
            self.code+=('@SP\n')   #Busco el tope de la pila
            self.code+=('A=M\n')   #Lo guardo en A
            self.code+=('M=D\n')   #Una vez alla pongo el dato que tenia en D
            self.code+=('@SP\n')   #Incremento SP
            self.code+=('M=M+1\n')
        elif command =='C_POP':
            self.code+='D=A\n'  #Guardo en D la dirección de destino
            self.code+='@R13\n' #Guardo en R13 lo qu tenia en D
            self.code+='M=D\n'
            self.code+='@SP\n'   #Busco el tope de la pila
            self.code+='AM=M-1\n' #Le resto uno y voy a esa posición
            self.code+='D=M\n'  #Guardo en D el dato del tope de la pila
            self.code+='@R13\n'  #Cargo la dirección de destino a A
            self.code+='A=M\n'
            self.code+='M=D\n'   #Y en esa posición guardo el dato que saqué 
        self.f.write(self.code) #Escribo todo en el archivo nuevo
        self.code = ''  


    def hallarDestino(self,segment,index):
        try:
            index=int(index)
        except ValueError:
            print("ERROR: El index "+index.strip() +" no es valido")
            exit(1)  
        #Defino la base de cada segmento, en constant no la necesito entonces para evitar KeyError pongo None
        valInicial={
            'local': 'LCL',
            'argument': 'ARG', 
            'this': 'THIS', 
            'that': 'THAT', 
            'pointer': 3, 
            'temp': 5, 
            'static': 16,
            'constant':None 
        }
        try:
            val = valInicial[segment] #Obtengo la base
        except(KeyError):
            print("ERROR: El segmento "+segment.strip() +" no existe")
            exit(1)

        if segment == 'constant':
           self.code+='@' + str(index)+'\n'    #Si es constant solo pongo el index directamentee  
        elif segment == 'static':
            self.code+='@' + self.filename + '.' + str(index)+'\n'  #Si es static creo una variable con el nombre del file y el index
        elif segment in ['pointer', 'temp']:
            self.code+='@R' + str(val + int(index))+'\n'     #Si es pointer o temp el sumo la base al index y obtengo la posicion
        elif segment in ['local', 'argument', 'this', 'that']: 
            self.code+='@' + val+'\n'          #Guardo la base en D
            self.code+='D=M\n'
            self.code+='@' + str(index)+'\n'  #Cargo en A el index y se lo sumo a la base
            self.code+='A=D+A\n'              #Dejo el resultado en A
        

    def close(self):
        self.code+='(END)\n'  #Ciclo infinito para cerrar cada programa
        self.code+='@END\n'
        self.code+='0;JMP\n'
        self.f.write(self.code)      
        self.f.close()        
        