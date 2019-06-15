class Code:
    @staticmethod
    def dest(command):
        if 'A' not in command and 'M' not in command and 'D' not in command and command !="":
            raise KeyError

        if 'A' in command:
            A = '1'
        else:
            A = '0'
        if 'D' in command:
            D = '1'
        else:
            D = '0'
        if 'M' in command:
            M = '1'
        else:
            M = '0'
        return A + D + M

    @staticmethod
    def comp(command):
        if "M" in command:
            a='1'
        else:
            a='0'    
        tabla = {
            '0':   '101010',
            '1':   '111111',
            '-1':  '111010',
            'D':   '001100',
            'A':   '110000',
            'M':   '110000',
            '!D':  '001101',
            '!A':  '110001',
            '!M':  '110001',
            '-D':  '001111',
            '-A':  '110011',
            '-M':  '110011',
            'D+1': '011111',
            'A+1': '110111',
            'M+1': '110111',
            'D-1': '001110',
            'A-1': '110010',
            'M-1': '110010',
            'D+A': '000010',
            'D+M': '000010',
            'D-A': '010011',
            'D-M': '010011',
            'A-D': '000111',
            'M-D': '000111',
            'D&A': '000000',
            'D&M': '000000',
            'D|A': '010101',
            'D|M': '010101'
        }
        return a + tabla[command]

    @staticmethod
    def jump(command):
        tabla = {
            '':    '000',
            'JGT': '001',
            'JEQ': '010',
            'JGE': '011',
            'JLT': '100',
            'JNE': '101',
            'JLE': '110',
            'JMP': '111'
        }
        return tabla[command]


