class code_writer:
    def __init__(self, filename):
        filewrite = filename.split('.vm') #Reemplazo el .vm con .asm si lo tiene 
        filewritef = filewrite[0]+'.asm'  #Sino le agrego el .asm
        try:
            self.f = open(filewritef, 'w')    #Abro el file en modo escribir
        except FileNotFoundError:
            print('ERROR:No hay directorio existente para escribir')   
            exit(1) 
        self.file=filename.split('.vm')[0].split("/")[-1]   #Nombre del file que estoy analizando
        if '\\' in self.file:                               #Si hay un backslash tomo lo último
            self.file=self.file.split('\\')[-1]
        self.code = ''      #Variable dodne ire acumulando lo que voy a escribir
        self.bool_count = 0 #Variable para saber cuantos gt ly o eq he hecho
        self.call_count=0   #Variable en la que ire contando los call
        self.currentFunction=''; #Funcion actual para escribir labels

    def setFileName(self, filename):  #Cambio el file que estoy analizando
        self.file=filename.split('.vm')[0].split('/')[-1] 
        if '\\' in self.file:
            self.file=self.file.split('\\')[-1] 

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
      command=command.strip()      #Elimino lineas nuevas
      if command in binary:
          self.code += '@SP\n'     #Busco tope de la pila
          self.code += 'M=M-1\n' 
          self.code += 'A=M\n' 
          self.code += 'D=M\n'     #Guardo el contenido en D
          self.code += 'A=A-1\n'   #Voy a la posicion anterior
          self.code = self.code+'M=M'+binary[command]+'D\n' #Aplico la operacion indicada con D
      elif command in unary:
          self.code += '@SP\n'     #Busco el tope de la pila
          self.code += 'A=M-1\n'   #Voy al elemento mas arriba
          self.code = self.code+'M='+unary[command]+'M\n' #Le aplico la operación unaria
      elif command in jump:
          self.code += '@SP\n'     #Busco el tope de la pila
          self.code += 'M=M-1\n' 
          self.code += 'A=M\n' 
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
                self.code+='D=M\n' #Guardo dato de la direccion 
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
            self.code+='M=M-1\n' #Le resto uno y voy a esa posición
            self.code+='A=M\n'
            self.code+='D=M\n'   #Guardo en D el dato del tope de la pila
            self.code+='@R13\n'  #Cargo la dirección de destino a A
            self.code+='A=M\n'
            self.code+='M=D\n'   #Y en esa posición guardo el dato que saqué        
        self.f.write(self.code)  #Escribo todo en el archivo nuevo
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
            self.code+='@' + self.file + '.' + str(index)+'\n'  #Si es static creo una variable con el nombre del file y el index
        elif segment in ['pointer', 'temp']:
            self.code+='@R' + str(val + int(index))+'\n'     #Si es pointer o temp el sumo la base al index y obtengo la posicion
        elif segment in ['local', 'argument', 'this', 'that']: 
            self.code+='@' + val+'\n'          #Guardo la base en D
            self.code+='D=M\n'
            self.code+='@' + str(index)+'\n'   #Cargo en A el index y se lo sumo a la base
            self.code+='A=D+A\n'               #Dejo el resultado en A
        
    def writeLabel(self,label):
        self.code=self.code+'('+ self.file+self.currentFunction+':'+label.upper().strip()+')'+'\n'   #Creo el label con el nombre del file , la fn y el label en mayuscula
        self.f.write(self.code) 
        self.code = ''  

    def writeGoto(self,label):
        self.code=self.code+'@'+self.file+self.currentFunction+':'+label.upper()+'\n' #Escribo el goto con el mismo formato del label
        self.code+='0;JMP\n' 
        self.f.write(self.code) 
        self.code = '' 

    def writeIf(self,label):
        self.code+='@SP\n'    #Hago pop de lo último en la pila
        self.code+='M=M-1\n' 
        self.code+='A=M\n'    
        self.code+='D=M\n'
        self.code=self.code+'@'+self.file+self.currentFunction+':'+label.upper()+'\n'   #Cargo en A el label con el formato indicado
        self.code+='D;JNE\n'     #Si el resultado del tope de la pila no es 0 hago el salto
        self.f.write(self.code) 
        self.code = ''

    def writeInit(self):
        self.code+='@256\n'            #Cargo 256 a SP 
        self.code+='D=A\n'
        self.code+='@SP\n'
        self.code+='M=D\n'             
        self.f.write(self.code) 
        self.code=''
        self.writeCall('Sys.init',0)  #Llamo Sys.init  

    def writeCall(self,functionName,numArgs):        
        retadd=functionName +'RET'+str(self.call_count) #Defino label de dir de ret
        self.call_count+=1                              #Sumo 1 al conteo de count

        self.pushRetAdd(retadd)
        self.writePushPointer('LCL')    # push LCL
        self.writePushPointer('ARG')    # push ARG
        self.writePushPointer('THIS')   # push THIS
        self.writePushPointer('THAT')   # push THAT

        self.code+=('@SP\n')      
        self.code+=('D=M\n')      #Cargo SP a D -> SP
        self.code+=('@LCL\n')   
        self.code+=('M=D\n')      #Pongo a LCL a apuntar a la misma dir de SP -> LCL=SP  

        self.code+=('@SP\n')     
        self.code+=('D=M\n')       #Cargo SP a D -> SP
        val = int(numArgs)+5       #Cuantifico el num de argumentos + 5
        vals=str(val)              #Lo paso a string para escribirlo
        self.code+=('@'+vals+'\n') #Cargo este valor en A
        self.code+=('D=D-A\n')     #A los que hay en D (SP), le resto el valor y lo guardo en D-> SP-n
        self.code+=('@ARG\n')     
        self.code+=('M=D\n')      #Pongo en ARG lo que calcule -> ARG=SP-n-5
        
        self.code+=('@'+functionName.replace(' ','')+'\n')  #Cargo la dirección de la funcion
        self.code+=('0;JMP\n')                              #Salto
        self.code+='('+retadd+')'+'\n'                      #Defino label para dirección de retorno
        self.f.write(self.code) 
        self.code = ''  
             
                
    def writeReturn(self): 
        self.code+=('@LCL\n')   #Pongo en D lo que tiene LCL
        self.code+=('D=M\n') 
        self.code+=('@R13\n')   #Frame lo tomo como R13
        self.code+=('M=D\n')    #Guardo ahí lo que tenía en D->FRAME=LCL

        self.code+=('@R13\n')   #Guardo en D lo que hay en frame -> FRAME
        self.code+=('D=M\n')    
        self.code+=('@5\n')     #Cargo 5 a A 
        self.code+=('D=D-A\n')  #Se lo resto a lo que hay en D --> FRAME-5
        self.code+=('A=D\n')    #Pongo en A la dirección que acabo de calcular 
        self.code+=('D=M\n')    #Cargo en D el contenido de esa dirección->*(FRAME-5)  
        self.code+=('@R14\n')   #Tomo RET como R14
        self.code+=('M=D\n')    #RET=*(FRAME-5)  

        self.code+='@SP\n'   
        self.code+='M=M-1\n' 
        self.code+='A=M\n' 
        self.code+='D=M\n'     # Hago pop()  y lo guardo en D 
        self.code+=('@ARG\n')   
        self.code+=('A=M\n')   # Pongo en A la dirección que tiene ARG
        self.code+=('M=D\n')   # Guardo ahí lo que tenía en D->*ARG=pop()  

        self.code+=('@ARG\n') 
        self.code+=('D=M\n')   #Guardo en D el contenido de ARG
        self.code+=('@SP\n') 
        self.code+=('M=D+1\n') #Guardo en SPlo que tengo en D +1 -> SP=ARG+1  

        self.setPointer('THAT','1')  #Hago push de THAT
        self.setPointer('THIS','2')  #Hago push de THIS
        self.setPointer('ARG','3')   #Hago push de ARG
        self.setPointer('LCL','4')   #Hago push de LCL

        self.code+=('@R14\n') 
        self.code+=('A=M\n')  #Pongo en A la dirección de RET
        self.code+=('0;JMP\n') #Salto -> goto RET   
        self.f.write(self.code) 
        self.code = ''                        

    def setPointer(self,var,index):
        self.code+=('@R13\n') 
        self.code+=('D=M\n')         #Pongo lo que tiene FRAME en D
        self.code+=('@'+index+'\n')  #Cargo lo que le voy a restar a A
        self.code+=('D=D-A\n')       #Se lo resto a lo que hay en D -> FRAME-index
        self.code+=('A=D\n')         #Cargo en A esta dirección
        self.code+=('D=M\n')         #Cargo en D el contenido -->*(FRAME-index)
        self.code+=('@'+var+'\n')    
        self.code+=('M=D\n')         #Guardo en val (THIS,THAT,ARG,LCL) lo que acabo de calcular --> THAT=*(FRAME-index)

    
    def writePushPointer(self,val):
        self.code+=('@'+val+'\n')
        self.code+=('D=M\n')   #Guardo en D lo que tiene val(THIS,THAT,LCL,ARG )
        self.code+=('@SP\n')   #Busco el tope de la pila
        self.code+=('A=M\n')   #Lo guardo en A
        self.code+=('M=D\n')   #Una vez alla pongo el dato que tenia en D
        self.code+=('@SP\n')   #Incremento SP
        self.code+=('M=M+1\n')

    def pushRetAdd(self,ret):
        self.code+=('@'+ret+'\n') #Cargo al dirección de retorno en A
        self.code+=('D=A\n')      #La guardo en D
        self.code+=('@SP\n') 
        self.code+=('A=M\n') 
        self.code+=('M=D\n')      #Voy al SP y pongo allí la dir de retorno
        self.code+=('@SP\n')   
        self.code+=('M=M+1\n')    #Incremento SP


    def writeFunction(self,functionName,numLocals):
        self.currentFunction=functionName   #La función actual es la que estoy traduciendo
        self.code+=('('+functionName.replace(" ", "")+')'+'\n')  #Pongo el label de la función
        for x in range(int(numLocals)):    #Por cada argumento
            self.code+=('D=0\n')           #Pongo en D un 0
            self.code+=('@SP\n') 
            self.code+=('A=M\n') 
            self.code+=('M=D\n')  
            self.code+=('@SP\n')   
            self.code+=('M=M+1\n')         #Hago push
        self.f.write(self.code) 
        self.code = ''    
            
    
    def closeAll(self):
        self.code+='(END)\n'  #Ciclo infinito para cerrar cada programa
        self.code+='@END\n'
        self.code+='0;JMP\n'
        self.f.write(self.code)
        self.code='' 
        self.f.close()  
