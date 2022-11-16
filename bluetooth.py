from machine import Pin,UART
import Temp
BT = UART(0,9600)

Temp_pin = 16
temp = Pin(Temp_pin, Pin.OUT)

while True:
    if BT.any():
        data = BT.write(1)
        print(data)
        if Temp < 20:
            print('Temperatura alta, tome precaucion')
            BT.write(' Temperatura alta, tome precaucion\n')
        elif Temp > 20:
            print('Estable \n')
            BT.write('Estable \n')