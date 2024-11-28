import serial
import time
import pyautogui
import re


ser = serial.Serial('COM3', 9600)  


def move(ax, ay):
    sensitivity = 2  
    dead_zone = 1500 

    
    if abs(ax) > dead_zone or abs(ay) > dead_zone:
      

        move_x = ay / 200 * sensitivity 
        move_y = ax / 200* sensitivity   
        
        
        pyautogui.moveRel(move_x, -move_y)
    else:
        print("waiting...")


def read_serial_data():
    while True:
        try:
        
            line = ser.readline().decode('utf-8', errors='ignore').strip()
            
            if "MPU6050 is connected" in line:
                print(line)  
            
            elif "MPU6050 connection failed" in line:
                print("Error: Unable to connect to the MPU6050.")
            
            
            elif "Accelerometer" in line:
            
                accel_data = re.findall(r"X:\s*(-?\d+)\s*Y:\s*(-?\d+)\s*Z:\s*(-?\d+)", line)
                
                if not accel_data:
                    print(f"Data error: Invalid accelerometer data in line: {line}")
                    continue
                
                
                ax, ay, az = map(int, accel_data[0])  
                
                
                move(ax, ay)  

        except Exception as e:
            print(f"Data error: {e}")


if __name__ == "__main__":
    read_serial_data()
