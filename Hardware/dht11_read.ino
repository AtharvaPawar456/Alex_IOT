#include "DHT.h"
#define DHTTYPE DHT11   // DHT 11

// DHT Sensor
uint8_t DHTPin = D8;               
// Initialize DHT sensor.
DHT dht(DHTPin, DHTTYPE);                
float Temperature;
float Humidity;
 
void setup() {
  Serial.begin(9600);
  delay(100);
  
  pinMode(DHTPin, INPUT);

  dht.begin();              
}
void loop() {
  
  handle_OnConnect();
  delay(100);
}

void handle_OnConnect() {

 Temperature = dht.readTemperature(); // Gets the values of the temperature
  Humidity = dht.readHumidity(); // Gets the values of the humidity 
Serial.print("Temperature:");
Serial.println(Temperature);

Serial.print("Humidity:");
Serial.println(Humidity);

}
