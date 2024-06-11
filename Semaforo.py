class ControladorSemáforo:
    def __init__(self):
        self.estado_actual = 'verde'

    def cambiar_estado(self):
        if self.estado_actual == 'verde':
            print("El semáforo está en verde. Se cambiará a amarillo.")
            self.estado_actual = 'amarillo'
        elif self.estado_actual == 'amarillo':
            print("El semáforo está en amarillo. Se cambiará a rojo.")
            self.estado_actual = 'rojo'
        elif self.estado_actual == 'rojo':
            print("El semáforo está en rojo. Se cambiará a verde.")
            self.estado_actual = 'verde'

# Uso
controlador = ControladorSemáforo()
controlador.cambiar_estado()  # El semáforo está en verde. Se cambiará a amarillo.
controlador.cambiar_estado()  # El semáforo está en amarillo. Se cambiará a rojo.
controlador.cambiar_estado()  # El semáforo está en rojo. Se cambiará a verde.
