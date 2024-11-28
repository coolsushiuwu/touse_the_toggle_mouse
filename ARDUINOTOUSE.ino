#include <Wire.h>
#include <MPU6050.h>

MPU6050 mpu;  

void setup() {
  Serial.begin(9600);  
  Wire.begin();     
  mpu.initialize();    


  if (mpu.testConnection()) {
    Serial.println("MPU6050 is connected.");
  } else {
    Serial.println("MPU6050 connection failed!");
  }
}

void loop() {
  
  int16_t ax, ay, az, gx, gy, gz;

  
  mpu.getAcceleration(&ax, &ay, &az);
  mpu.getRotation(&gx, &gy, &gz);

  
  Serial.print("Accelerometer X: ");
  Serial.print(ax);
  Serial.print(" Y: ");
  Serial.print(ay);
  Serial.print(" Z: ");
  Serial.print(az);
  
  Serial.print(" | Gyroscope X: ");
  Serial.print(gx);
  Serial.print(" Y: ");
  Serial.print(gy);
  Serial.print(" Z: ");
  Serial.println(gz);

  delay(100);  
}
