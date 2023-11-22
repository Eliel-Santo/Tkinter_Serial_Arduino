import serial
import json
import time



# https://stackoverflow.com/questions/2785821/is-there-an-easy-way-in-python-to-wait-until-certain-condition-is-true
def wait_until(somepredicate, timeout, period=0.25, *args, **kwargs):
  mustend = time.time() + timeout
  while time.time() < mustend:
    if somepredicate: return True
    time.sleep(period)
  return False


# make sure the 'COM#' is set according the Windows Device Manager
ser = serial.Serial('COM3', 9600, timeout=1)
# ser.reset_input_buffer()


# Creating Json
data = {}
data["led1"] = 1
data["led2"] = 255
data["led3"] = 0

# data = {"led1": 1, "led2": 0, "led1_pwm": 0, "led2_pwm": 0}

data = json.dumps(data) # Sending JSon:  {"led1": 255,"led2": 255,"led3":0}
print(data)

if wait_until(ser.inWaiting() != 0,1) == False:
    wait_until(ser.inWaiting() != 0,1)

print("Status Waiting: " + str(ser.inWaiting()!=0))
print("Serial Waiting: " + str(ser.inWaiting()))

# ser.inWaiting() > 0
while(ser.inWaiting() > 0):
    line = ser.readline().decode("utf-8")  # read a byte string
    # ser.reset_input_buffer() # Apaga o buffer

    try:
        dict_json = json.loads(line)
        print(dict_json)
        Botao1 = dict_json.get("Botao1")
        Botao2 = dict_json.get("Botao2")
        print("Botão 1: " + str(Botao1) + '\n' + "Botão 2: " + str(Botao2))

    except json.JSONDecodeError as e:
        a=1
        # print("JSON:", e) #Print o erro
        # print(line)


ser.close()
