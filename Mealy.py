class MaquinaMealy:
    def __init__(self, estados, alfabeto, transiciones, salidas, estado_inicial):
        self.estados = estados
        self.alfabeto = alfabeto
        self.transiciones = transiciones
        self.salidas = salidas
        self.estado = estado_inicial

    def transicion(self, simbolo_entrada):
        par_estado_entrada = (self.estado, simbolo_entrada)
        if par_estado_entrada in self.transiciones:
            self.estado = self.transiciones[par_estado_entrada]
            return self.salidas[par_estado_entrada]
        else:
            raise ValueError("Símbolo de entrada o estado inválido")

# Definición de estados, alfabeto, transiciones y salidas
estados = {'A', 'B'}
alfabeto = {'0', '1'}
transiciones = {('A', '0'): 'A', ('A', '1'): 'B', ('B', '0'): 'A', ('B', '1'): 'B'}
salidas = {('A', '0'): 0, ('A', '1'): 1, ('B', '0'): 1, ('B', '1'): 0}
estado_inicial = 'A'

# Crear la máquina de estado Mealy
maquina_mealy = MaquinaMealy(estados, alfabeto, transiciones, salidas, estado_inicial)

# Ejecutar una secuencia de entradas
entradas = ['0', '1', '0', '1', '1']
for simbolo_entrada in entradas:
    salida = maquina_mealy.transicion(simbolo_entrada)
    print(f"Entrada: {simbolo_entrada}, Salida: {salida}, Estado: {maquina_mealy.estado}")
