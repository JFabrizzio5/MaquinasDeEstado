class MooreMachine:
    def __init__(self, states, alphabet, transitions, outputs, initial_state):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.outputs = outputs
        self.state = initial_state

    def transition(self, input_symbol):
        if (self.state, input_symbol) in self.transitions:
            self.state = self.transitions[(self.state, input_symbol)]
        else:
            raise ValueError("Invalid input symbol or state")

    def output(self):
        return self.outputs[self.state]

# Definición de estados, alfabeto, transiciones y salidas
states = {'A', 'B'}
alphabet = {'0', '1'}
transitions = {('A', '0'): 'A', ('A', '1'): 'B', ('B', '0'): 'A', ('B', '1'): 'B'}
outputs = {'A': 0, 'B': 1}
initial_state = 'A'

# Crear la máquina de estado Moore
moore_machine = MooreMachine(states, alphabet, transitions, outputs, initial_state)

# Ejecutar una secuencia de entradas
inputs = ['0', '1', '0', '1', '1']
for input_symbol in inputs:
    moore_machine.transition(input_symbol)
    output = moore_machine.output()
    print(f"Input: {input_symbol}, Output: {output}, State: {moore_machine.state}")
