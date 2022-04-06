//--------------projectswithpawar.in-------------//
#include "ThingSpeak.h"
#include <ESP8266WiFi.h>

const char ssid[] = "MAHAKAL";  // your network SSID (name)
const char pass[] = "sateri456";   // your network password 

#include "DHT.h"
#define DHTTYPE DHT11   // DHT 11

// DHT Sensor
uint8_t DHTPin = D8;               
// Initialize DHT sensor.
DHT dht(DHTPin, DHTTYPE);                
float Temperature;
float Humidity;

#define LED1 D0  // LED at  D0
#define LED2 D1  // LED at  D1
#define LED3 D2  // LED at  D2
#define LED4 D3  // LED at  D3

WiFiClient  client;

//---------Channel Details---------//
unsigned long counterChannelNumber = 1661789;            // Channel ID
const char * myCounterReadAPIKey = "BWRV718JS99HRK3N"; // Read API Key
const char * myWriteAPIKey = "YYN5LAINXD8Y6Y4A"; // write API key

const int FieldNumber1 = 1;  // read
//const int FieldNumber2 = 2;  // write
//const int FieldNumber3 = 3;  // write
//-------------------------------//
int prev = 0;

void setup()
{
  Serial.begin(9600);
  WiFi.mode(WIFI_STA);
  ThingSpeak.begin(client);
  
  pinMode(LED1, OUTPUT);digitalWrite(LED1, LOW);
  pinMode(LED2, OUTPUT);digitalWrite(LED2, LOW);
  pinMode(LED3, OUTPUT);digitalWrite(LED3, LOW);
  pinMode(LED4, OUTPUT);digitalWrite(LED4, LOW);
  
  pinMode(DHTPin, INPUT);
  dht.begin();
  
}

void loop()
{
  //----------------- Network -----------------//
  if (WiFi.status() != WL_CONNECTED)
  {
    Serial.print("Connecting to ");
    Serial.print(ssid);
    Serial.println(" ....");
    while (WiFi.status() != WL_CONNECTED)
    {
      WiFi.begin(ssid, pass);
      delay(5000);
    }
    Serial.println("Connected to Wi-Fi Succesfully.");
  }
  //--------- End of Network connection--------//

  //---------------- Channel 1 ----------------//
  long temp = ThingSpeak.readLongField(counterChannelNumber, FieldNumber1, myCounterReadAPIKey);
  int statusCode = ThingSpeak.getLastReadStatus();

  Temperature = dht.readTemperature(); // Gets the values of the temperature
  Humidity = dht.readHumidity(); // Gets the values of the humidity 


  //ThingSpeak.writeField(counterChannelNumber, 2, Temperature, myWriteAPIKey);
  //delay(150);
  //ThingSpeak.writeField(counterChannelNumber, 3, Humidity, myWriteAPIKey);
  //delay(150);
//  value = "";
  
  delay(10);

  Serial.print("temp: ");
  Serial.println(temp);

  //Serial.print("statusCode: ");
  //Serial.print(statusCode);
  if (statusCode == 200)
  {
    if (prev != temp){

    
    Serial.print("Temperature:");
    Serial.println(Temperature);
    
    Serial.print("Humidity:");
    Serial.println(Humidity);
      
    Serial.print("Field 1: ");
    Serial.println(temp);
    
    if (temp == 450){         digitalWrite(LED1, LOW);}
    if (temp == 400){         digitalWrite(LED1, HIGH);}
    
    if (temp == 550){         digitalWrite(LED2, LOW);}
    if (temp == 500){         digitalWrite(LED2, HIGH);}
    
    if (temp == 650){         digitalWrite(LED3, LOW);}
    if (temp == 600){         digitalWrite(LED3, HIGH);}
    
    if (temp == 750){         digitalWrite(LED4, LOW);}
    if (temp == 700){         digitalWrite(LED4, HIGH);}

    if (temp == 750){         digitalWrite(LED4, LOW);}
    if (temp == 700){         digitalWrite(LED4, HIGH);}

    if (temp == 800){         
      ThingSpeak.writeField(counterChannelNumber, 2, Temperature, myWriteAPIKey);
      Serial.println("===Temperature updated on TS===");
      delay(150);
      ThingSpeak.writeField(counterChannelNumber, 3, Humidity, myWriteAPIKey);
      Serial.println("===Humidity updated on TS===");
      Serial.println("_");
      }
      prev = temp;
    }
    Serial.print("stable");

  }
  else
  {
    Serial.println("Unable to read channel / No internet connection");
  }
  delay(10000);
}
