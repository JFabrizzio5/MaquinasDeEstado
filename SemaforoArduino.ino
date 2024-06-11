// Definición de pines para los LEDs
const int pinVerde = 1;
const int pinAmarillo = 2;
const int pinRojo = 3;

// Definición de estados del semáforo
enum EstadoSemaforo {
  VERDE,
  AMARILLO,
  ROJO
};

// Inicialización del estado del semáforo
EstadoSemaforo estadoActual = AMARILLO;

// Función para cambiar el estado del semáforo
void cambiarEstado() {
  switch (estadoActual) {
    case VERDE:
      digitalWrite(pinVerde, LOW);
      digitalWrite(pinAmarillo, HIGH);
      delay(2000); // Tiempo de espera en amarillo
      estadoActual = AMARILLO;
      break;
    case AMARILLO:
      digitalWrite(pinAmarillo, LOW);
      digitalWrite(pinRojo, HIGH);
      delay(2000); // Tiempo de espera en rojo
      estadoActual = ROJO;
      break;
    case ROJO:
      digitalWrite(pinRojo, LOW);
      digitalWrite(pinVerde, HIGH);
      delay(2000); // Tiempo de espera en verde
      estadoActual = VERDE;
      break;
  }
}

void setup() {
  // Inicialización de pines como salida
  pinMode(pinVerde, OUTPUT);
  pinMode(pinAmarillo, OUTPUT);
  pinMode(pinRojo, OUTPUT);
}

void loop() {
  cambiarEstado(); // Cambiar el estado del semáforo
}
