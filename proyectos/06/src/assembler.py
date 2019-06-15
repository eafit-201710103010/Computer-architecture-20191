from code import Code
from symbols import SymbolsTable
from assemblerParser import Parser
import sys

#Lectura de argumenos
arg = sys.argv
if len(arg)<2:
    print("ERROR:No se dieron suficientes argumentos")
    exit(1)
dir = arg[1]
if not ".asm" in dir:
    print("ERROR: El archivo no es .asm")
    exit(1)
nout = dir.split('.asm') 
nout =nout[0] + ".hack"
out1=""
#Inicialización de contadores y parser inicial
countROM=0
countRAM=16
parser1=Parser(dir)
simbolos = SymbolsTable()
#Primera pasada
while parser1.hasMoreCommands():
    parser1.advance()
    tipo = parser1.commandType()
    if tipo=="L_COMMAND":
        #Obtener simbolo a buscar
        var = parser1.symbol()
        #De no existir, agregarlo
        if not simbolos.contains(var):
            simbolos.addEntry(var,countROM)
    else:
        #Contar instrucciones A y C
         countROM+=1    

#Segunda pasada, se inicializa otra vez el Parser
parser2 =Parser(dir)       
while parser2.hasMoreCommands():
    parser2.advance()   
    tipo=parser2.commandType()
    if tipo=="C_COMMAND":
        #Inicio de toda instrucción C
        inst="111"
        #Obtengo código según lo indicado por el parser
        try:
            comp =parser2.comp()
            inst=inst+Code.comp(comp)  
            dest= parser2.dest() 
            inst=inst+Code.dest(dest)
            jump=parser2.jump()
            inst=inst+Code.jump(jump)
        except KeyError:
            print("ERROR: Argumentos no validos en instruccion C en el comando: "+parser2.currentCommand)
            exit(1)    
        #Agrego el resto de la instrucción
        out1=out1+inst+'\n'
    elif tipo=="A_COMMAND":
        sim = parser2.symbol()
        #Si es númerico paso directamente a binario
        if sim.isnumeric():
            num =int(sim)
            b=format(num, "016b")
            out1=out1+b+'\n'
        else:
            #Si existe en la tabla de simbolos, obtengo el valor y lo convierto a binario
            if simbolos.contains(sim):
                sim= simbolos.GetAddress(sim)   
                num= int(sim)
                b=format(num, "016b")
                out1=out1+b+'\n'
            elif sim!= "":
                #Si no existe lo agrego a la tabla y traduzco a binario
                simbolos.addEntry(sim,countRAM)
                countRAM+=1
                sim= simbolos.GetAddress(sim)   
                num= int(sim)
                b=format(num, "016b")
                out1=out1+b+'\n' 
            else:
                print("ERROR: No se dan parámetros para instrucción A en el comando: "+parser2.currentCommand())  
                exit(1)    

out= open(nout,'w')
out.write(out1)        
