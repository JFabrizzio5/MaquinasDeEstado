class ControladorReproduccionMusica:
    def __init__(self):
        self.estado_actual = 'pausado'

    def reproducir(self):
        if self.estado_actual == 'pausado':
            print("Reproduciendo música.")
            self.estado_actual = 'reproduciendo'
        else:
            print("La música ya se está reproduciendo.")

    def pausar(self):
        if self.estado_actual == 'reproduciendo':
            print("Música pausada.")
            self.estado_actual = 'pausado'
        else:
            print("La música ya está pausada.")

    def detener(self):
        if self.estado_actual == 'reproduciendo':
            print("Música detenida.")
            self.estado_actual = 'detenido'
        else:
            print("La música ya está detenida.")

# Uso
controlador_musica = ControladorReproduccionMusica()
controlador_musica.reproducir()  # Reproduciendo música.
controlador_musica.pausar()     # Música pausada.
controlador_musica.reproducir()  # Reproduciendo música.
controlador_musica.detener()    # Música detenida.
