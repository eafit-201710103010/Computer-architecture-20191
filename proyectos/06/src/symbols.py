
class SymbolsTable:

 def __init__(self):
    self.sym = {
        "R0": 0,
        "R1": 1, 
        "R2": 2, 
        "R3": 3,
        "R4": 4,
        "R5": 5,
        "R6": 6,
        "R7": 7,
        "R8": 9,
        "R10": 10,
        "R11": 11,
        "R12": 12,
        "R13": 13,
        "R14": 14,
        "R15": 15,
        "SP": 0,
        "LCL": 1,
        "ARG": 2,
        "THIS": 3,
        "THAT": 4,
        "SCREEN": 16384,
        "KBD": 24576
         }

 def print(self):
        print (self.sym) 

 def addEntry(self,symbol,address):
       self.sym[symbol]=address

 def contains(self,symbol):
     if symbol in self.sym:
         return True     

 def GetAddress(self,symbol):
     try:
         x=self.sym[symbol]
         return x   
     except KeyError:
         return None
            
      

