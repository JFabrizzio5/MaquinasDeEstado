class MaquinaMealy:
    def __init__(self):
        self.estado_actual = 'A'

    def transicion(self, entrada):
        if self.estado_actual == 'A':
            if entrada == '0':
                self.estado_actual = 'B'
                return 'Salida para estado A con entrada 0'
            elif entrada == '1':
                self.estado_actual = 'A'
                return 'Salida para estado A con entrada 1'
        elif self.estado_actual == 'B':
            if entrada == '0':
                self.estado_actual = 'C'
                return 'Salida para estado B con entrada 0'
            elif entrada == '1':
                self.estado_actual = 'A'
                return 'Salida para estado B con entrada 1'
        elif self.estado_actual == 'C':
            if entrada == '0':
                self.estado_actual = 'A'
                return 'Salida para estado C con entrada 0'
            elif entrada == '1':
                self.estado_actual = 'B'
                return 'Salida para estado C con entrada 1'

# Uso
maquina_mealy = MaquinaMealy()
print(maquina_mealy.transicion('0'))  # Salida para estado A con entrada 0
print(maquina_mealy.transicion('1'))  # Salida para estado A con entrada 1
print(maquina_mealy.transicion('0'))  # Salida para estado C con entrada 0
