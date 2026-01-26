#include <Wire.h>
#include <Adafruit_sensor.h>
#include <Adafruit_BMP280.h>

Adafruit_BMP280 bmp;

float temperatura
float presion
// Faltaria una variable que nos diga que si el cohete que soltó el satelite o no bool puede ser


const int intervalo_lectura = 100

void setup() {
  Serial.begin(); /*nº de baudios que hacen falta*/
  while(!Serial) delay(10);
  
  if (!bmp.begin()){ /*direccion I2C*/
    Serial.println("No ha encontrado el Sensor BMP280")
  while(1) delay(10) /* repite el programa hasta que se encuentre el sensor con un delay de 10MS*/
  }
  Serial.println("Sensor encontrado")

  bmp.setsampling(Adafruit_BMP280::MODE_NORMAL, 
                  Adafruit_BMP280:: SAMPLING_X16,
                  Adafruit_BMP280:: SAMPLING_X16,
                  Adafruit_BMP280:: FILTER_X16,
                  Adafruit_BMP280:: STANDBY_MS_1);  
}




void loop() {
  float temperatura = bmp.readTemperature();
  float presion = bmp.readPressure() / 100.0; /*Leemos en hectopascales ya que es la unidad de presion atmosferica*/

  serial.print("Temperatura:");
  Serial.print(temperatura);
  Serial.println(" ºC");

  Serial.print("Presion: ");
  Serial.print(presion);
  Serial.println(" hPa");

  Serial.println("----------------------");


  delay(/*Tiempo de la siguiente lectura*/)


}
