class SymbolTable:
    clase = {}
    subrutina= {}
    conts = {'static':0, 'field':0, 'argument':0, 'local':0}

    def __init__(self):
        self.conts['field']  = 0
        self.subrutina = {}

    def startSubroutine(self):
        """Inicializa la lista simbolos de la subrutina """
        self.subrutina= {}
        self.conts['argument'] = 0
        self.conts['local'] = 0

    def define(self,name,tipo,kind):
        """Ingresa un nuevo simbolo a la tabla de simbolos dependiendo de su tipo y segmento, usando los indices calculados"""
        tipos = str(tipo)
        nombre = str(name)
        kinds = str(kind)
        numero = 0
        if kinds == 'argument':
            numero = self.conts['argument']
            self.subrutina[nombre] = [tipos,kinds,numero]
            self.conts['argument'] += 1
        elif kinds == 'local':
            numero = self.conts['local']
            self.subrutina[nombre] = [tipos,kinds,numero]
            self.conts['local'] += 1
        elif kinds  == 'static':
            numero = self.conts['static']
            self.clase[nombre] = [tipos,kinds,numero]
            self.conts['static'] += 1
        elif kinds == 'field':
            numero = self.conts['field']
            self.clase[nombre] = [tipos,kinds,numero]
            self.conts['field'] += 1
                
    
    def varCount(self, kind):
        """Retirna la cuenta que se lleva de algun segmento"""
        kinds = str(kind)
        return self.conts[kinds]
    
    def kindOf(self, name):
        """Retorna donde se puede encontrar una variable"""
        nombre = str(name)
        if nombre in self.clase.keys():
            if self.clase[nombre][1] == 'field':
                return 'this'
            else:
                return self.clase[nombre][1]
        elif nombre in self.subrutina.keys():
            if self.subrutina[nombre][1] == 'field':
                return 'this'
            else:
                return self.subrutina[nombre][1]
        else:
            return None

    def typeOf(self,name):
        """Retorna el tipo de dato de una variable"""
        nombre = str(name)
        if nombre in self.clase.keys():
            return self.clase[nombre][0]
        elif nombre in self.subrutina.keys():
            return self.subrutina[nombre][0]

    def indexOf(self,name):
        """Retorna le indice en que se encuentra un simbolo en la tabla"""
        nombre = str(name)
        if nombre in self.clase.keys():
            return self.clase[nombre][2]
        elif nombre in self.subrutina.keys():
            return self.subrutina[nombre][2]