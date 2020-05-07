#include <ESP8266HTTPClient.h>
#include <ESP8266WiFi.h>
#include "json/json.h"
#include <ArduinoJson.h>



void counting_windspeed();
void counting_buckets();
String Heading(int);
unsigned long int lastDebounceTime_wind = 0;
unsigned long int lastDebounceTime_bucket = 0;
int debounceDelay = 10;
int  count_wind;
int  count_bucket;
int VaneValue;
int Direction;
int CalDirection;
int LastValue = 1;
int Offset = 0;
String dir;
unsigned long int start_time;
unsigned long int last_time;

void setup() {
  pinMode(D1, INPUT);
  pinMode(D2, INPUT);
  pinMode(A0, INPUT);
  count_wind = 0;
  count_bucket = 0;
  attachInterrupt(digitalPinToInterrupt(D1), counting_windspeed, FALLING);
  attachInterrupt(digitalPinToInterrupt(D2), counting_buckets, FALLING);
  Serial.begin(115200);
  WiFi.begin("anu", "anagha12");   //WiFi connection

  while (WiFi.status() != WL_CONNECTED) {  //Wait for the WiFI connection completion

    delay(500);
    Serial.println("Waiting for connection");

  }
  start_time = millis();
  last_time = millis();
}
void loop()
{


  sei();
  //delay(3000);
  //cli();
  if ((millis() - last_time) > 10000)
  {
    count_wind = 0;
    count_bucket = 0;
    last_time = start_time;
    start_time = millis();
  }

  VaneValue = analogRead(A0);
  Direction = map(VaneValue, 0, 1023, 0, 360);
  CalDirection = Direction + Offset;
  while (CalDirection > 360) {
    CalDirection = CalDirection - 360;
  }
  while (CalDirection < 0) {
    CalDirection = CalDirection + 360;
  }


  if (abs(CalDirection - LastValue) > 1)
  {
    //Serial.print("direction=");
    dir = Heading(CalDirection);
    // Serial.print("count_wind="); Serial.println(count_wind); Serial.print("\t");
    // Serial.print("count_bucket="); Serial.println(count_bucket); Serial.println("\t");

    LastValue = CalDirection;

  }
  if (WiFi.status() == WL_CONNECTED) {

    HTTPClient http;
    DynamicJsonDocument doc(1024);
    doc["wind_count"] = count_wind;
    doc["bucket_count"] = count_bucket;
    doc["direction"] = dir;
    String json;
    serializeJson(doc, json);
    Serial.println(json);

    http.begin("http://192.168.43.89:5000/weatherstation");
    http.addHeader("Content-Type", "application/json");
    int httpCode = http.POST(json);
    String payload = http.getString();

    Serial.println(httpCode);
    Serial.println(payload);

    http.end();
  } else {

    Serial.println("Error in WiFi connection");

  }
}

void counting_windspeed() {

  if ((millis() - lastDebounceTime_wind) > debounceDelay) {
    count_wind = count_wind + 1;
    lastDebounceTime_wind = millis();
  }
}
void counting_buckets() {

  if ((millis() - lastDebounceTime_bucket) > debounceDelay) {
    count_bucket = count_bucket + 1;
    lastDebounceTime_bucket = millis();
  }
}

String Heading(int direction) {
  if (direction < 22)
  {
    Serial.println("E\n");
    return ("E");
  }
  else if (direction < 67)
  {
    Serial.println("W\n");
    return ("W");
  }
  else if (direction < 112)
  {
    Serial.println("NW\n");
    return ("NW");
  }
  else if (direction < 157)
  {
    Serial.println("N\n");
    return ("N");
  }

  else if (direction < 212) {
    Serial.println("SW");
    return ("SW");
  }
  else if (direction < 247) {
    Serial.println("NE\n");
    return ("NE");
  }

  else if (direction < 292) {
    Serial.println("S\n");
    return ("S");
  }
  else if (direction < 337) {
    Serial.println("SE\n");
    return ("SE");
  }
  else
  { Serial.println("E\n");
    return ("E");
  }
}
