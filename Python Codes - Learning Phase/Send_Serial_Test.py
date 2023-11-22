import serial
import json
import time







# make sure the 'COM#' is set according the Windows Device Manager
ser = serial.Serial('COM3', 9600, timeout=1)
# ser.reset_input_buffer()

time.sleep(5)

data = {"led1": 1, "led2": 0, "led1_pwm": 0, "led2_pwm": 0}

data = json.dumps(data) # Sending JSon:  {"led1": 255,"led2": 255,"led3":0}
x = 'a'
ser.write(bytes(data, 'utf-8'))

print(data)

while(True):
    a=1


ser.close()
