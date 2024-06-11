class MaquinaMoore:
    def __init__(self):
        self.estado_actual = 'A'

    def transicion(self, entrada):
        if self.estado_actual == 'A':
            if entrada == '0':
                self.estado_actual = 'B'
                return 'Salida para estado B'
            elif entrada == '1':
                self.estado_actual = 'A'
                return 'Salida para estado A'
        elif self.estado_actual == 'B':
            if entrada == '0':
                self.estado_actual = 'C'
                return 'Salida para estado C'
            elif entrada == '1':
                self.estado_actual = 'A'
                return 'Salida para estado A'
        elif self.estado_actual == 'C':
            if entrada == '0':
                self.estado_actual = 'A'
                return 'Salida para estado A'
            elif entrada == '1':
                self.estado_actual = 'B'
                return 'Salida para estado B'

# Uso
maquina_moore = MaquinaMoore()
print(maquina_moore.transicion('0'))  # Salida para estado B
print(maquina_moore.transicion('1'))  # Salida para estado A
print(maquina_moore.transicion('0'))  # Salida para estado C
