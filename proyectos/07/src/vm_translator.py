import sys
from vm_parser import Parser
from vm_code_writer import code_writer
#Obtengo el nombre del file
file_path = sys.argv[1]
#Creo parser y code writer
parser = Parser(file_path)
cw = code_writer(file_path)
#Itero por cada linea
while parser.hasMoreCommands():
    parser.advance()
    if parser.commandType() == 'C_PUSH':
        cw.writePushPop('C_PUSH', parser.arg1(), parser.arg2())
    elif parser.commandType() == 'C_POP':
        cw.writePushPop('C_POP', parser.arg1(), parser.arg2())
    elif parser.commandType() == 'C_ARITHMETIC':
        cw.writeArithmetic(parser.arg1())
cw.close()