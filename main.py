from machine import PWM, I2C,Pin
from BH1750 import BH1750
from time import sleep
import utime
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

#Dirección del I2C y tamaño del LCD
I2C_ADDR  =  0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20

def main():
    i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
    lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)

#i2c = I2C(0,sda=Pin(16), scl=Pin(17), freq=400000)

#light = BH1750(i2c)

#salida = PWM(Pin(18))

#salida.freq(1000)

#led_1 = Pin(25,Pin.OUT)

    while True:
    #led_1.value(1)
    #lux=light.luminance(BH1750.ONCE_HIRES_1)  ## Sample luminance in lux
    #print(lux)
    #voltaje = int(lux * 65535 / 1000)
    #salida.duty_u16(voltaje)
    #sleep(0.1)
    lcd.clear()
    lcd.move_to(0,0)
    lcd.putstr("Suscribete a   ")
    utime.sleep(1)
    lcd.move_to(0,1)
    lcd.putstr("Control    ")
    utime.sleep(1)
    
if __name__ == '__main__':
    main()
