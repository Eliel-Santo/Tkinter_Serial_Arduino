from serial import *
from threading import Thread
from time import sleep
import json




last_received = ''

def receiving(ser):
    global last_received
    corretos = 0
    errados = 0
    buffer_string = ''
    while True:
        if ser.inWaiting() > 0:
            buffer_string = buffer_string + ser.read(ser.inWaiting()).decode()
            if '\n' in buffer_string:
                lines = buffer_string.split('\n') # Guaranteed to have at least 2 entries
                last_received = lines[-2]
                #If the Arduino sends lots of empty lines, you'll lose the
                #last filled line, so you could make the above statement conditional
                #like so: if lines[-2]: last_received = lines[-2]
                buffer_string = lines[-1]
                # sleep(0.1)

            # print(buffer_string)

            try:
                dict_json = json.loads(buffer_string)
                corretos = corretos + 1
                # print(dict_json)

            except json.JSONDecodeError as e:
                errados = errados + 1

            print(buffer_string)
            # print(str(corretos) + "/" + str(errados + corretos) + " = " + str(round(100*corretos/(corretos + errados),3)) + "% " + "=> Errados: " + str(errados))









if __name__ ==  '__main__':
    ser = Serial(
        port="COM3",
        baudrate=9600,
        bytesize=EIGHTBITS,
        parity=PARITY_NONE,
        stopbits=STOPBITS_ONE,
        timeout=0.1,
        xonxoff=0,
        rtscts=0,
        interCharTimeout=None
    )

    Thread(target=receiving, args=(ser,)).start()