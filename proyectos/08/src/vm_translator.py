import sys
import os
from vm_parser import Parser
from vm_code_writer import code_writer

#Si es un directorio
if len(sys.argv)==2 and '.vm' not in sys.argv[1]:
    #Si le falta el último slash se lo agrego para evitar errores en dirección
    if sys.argv[1][-1] != '/':
        sys.argv[1]=sys.argv[1]+'/'
    #El nombre del archivo .asm a generar es el mismo del directorio
    outname= sys.argv[1][:-1]+'/'+sys.argv[1].split('/')[-2]
    dirs = []
    # Voy por cada f (file) en el directorio y lo agrego a la lista de archivos a traducir
    for r, d, f in os.walk(sys.argv[1]):
        for file in f:
            #Solo tomo los .vm
            if '.vm' in file:
                dirs.append(os.path.join(r, file))    
#Si es un archivo .vm lo tomo solito                
else:
    dirs=sys.argv
    del dirs[0]
    outname=dirs[0].split('.vm')[0]
#Creo el codewriter con el nombre del archivo en el cual voy a escribir                  
cw = code_writer(outname)
#Si es un directorio escribo el llamado a Sys.init
if len(dirs)>1:
    cw.writeInit()
#Itero sobre cada file    
for file_path in dirs:  
    #Creo parser y  pongo el codewriter con el file que estoy analizando
    parser = Parser(file_path)
    cw.setFileName(file_path)
    # Itero por cada linea   
    while parser.hasMoreCommands():
        parser.advance()
        if parser.commandType() == 'C_PUSH':
            cw.writePushPop('C_PUSH', parser.arg1(), parser.arg2())
        elif parser.commandType() == 'C_POP':
            cw.writePushPop('C_POP', parser.arg1(), parser.arg2())
        elif parser.commandType() == 'C_ARITHMETIC':
            cw.writeArithmetic(parser.arg1())
        elif parser.commandType() == 'C_LABEL':
            cw.writeLabel(parser.arg1())
        elif parser.commandType() == 'C_IF':
            cw.writeIf(parser.arg1())
        elif parser.commandType() == 'C_GOTO':
            cw.writeGoto(parser.arg1())
        elif parser.commandType() == 'C_CALL':
            cw.writeCall(parser.arg1(), parser.arg2())
        elif parser.commandType() == 'C_FUNCTION':
            cw.writeFunction(parser.arg1(), parser.arg2())
        elif parser.commandType() == 'C_RETURN':
            cw.writeReturn()
cw.closeAll()    
