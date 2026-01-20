#include <Adafruit_BMP280.h>

Adafruit_BMP280 bmp; // Crear instancia del sensor

// Ajusta esto a la presión actual a nivel del mar en tu zona (hPa)
float seaLevelPressure = 1013.25; 

void setup() {
  Serial.begin(9600);
  Serial.println(F("=== BMP280 SENSOR PRUEBA ==="));

  if (!bmp.begin()) {
    Serial.println(F("ERROR: Sensor no encontrado. Conecte el sensor."));
    while (1); // Detener el programa
  }

  // Configuración de muestreo
  bmp.setSampling(
    Adafruit_BMP280::MODE_NORMAL,   // Modo de operación
    Adafruit_BMP280::SAMPLING_X2,   // Oversampling temperatura
    Adafruit_BMP280::SAMPLING_X16,  // Oversampling presión
    Adafruit_BMP280::FILTER_X16,    // Filtro
    Adafruit_BMP280::STANDBY_MS_500 // Tiempo Standby
  );
}

void loop() {
  float temperatureC = bmp.readTemperature();
  float temperatureF = temperatureC * 9 / 5 + 32;
  float pressurePa = bmp.readPressure();
  float pressurehPa = pressurePa / 100.0;
  float altitudeM = bmp.readAltitude(seaLevelPressure);

  Serial.println(F("----------------------------"));
  Serial.print(F("Temperatura: "));
  Serial.print(temperatureC, 2);
  Serial.print(" °C / ");
  Serial.print(temperatureF, 2);
  Serial.println(" °F");

  Serial.print(F("Presión: "));
  Serial.print(pressurePa, 2);
  Serial.print(" Pa / ");
  Serial.print(pressurehPa, 2);
  Serial.println(" hPa");

  Serial.print(F("Altitud aproximada: "));
  Serial.print(altitudeM, 2);
  Serial.println(" m");

  delay(2000); // Espera 2 segundos
}
