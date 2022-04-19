import machine
from machine import Pin
from machine import I2C
import ssd1306
import time
from time import sleep


i2c = I2C(scl=Pin(5), sda=Pin(4))

# screen dimmensions
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)


btnUp = Pin(14, Pin.IN, Pin.PULL_UP) #input pin 14 - internal resistance pull-up
btnDown = Pin(12, Pin.IN, Pin.PULL_UP) #input pin 12 - internal resistance pull-up


Pulse = machine.Pin(0)
Pulse0 = machine.PWM(Pulse)


Pulse0.freq(50)
Pulse0.duty(511)

value_duty = 1
frecuencia = (Pulse0.freq())
pulse_width = 1 / frecuencia
width = pulse_width * 1000
ancho_ms = str(width)

while True: 

    if not btnUp():  # increases duty cycle
        time.sleep_ms(160)
        value_duty = value_duty + 10
        if value_duty >= 1023:
          value_duty = 1023

    if not btnDown(): # decreases duty cycle
        time.sleep_ms(160)
        value_duty = value_duty - 10
        if value_duty <= 0:
          value_duty = 0

    led0.duty(value_duty) # adds value to PWM output

    valor_ciclo = int(value_duty)
    valor_ciclo *= 100
    valor_ciclo //= 1023
    ciclo = str(valor_ciclo)

    oled.text('MOTOR DRIVE', 14, 5)
    oled.text('DC = ', 0, 22)
    oled.text(ciclo, 40, 22)
    oled.text('%', 58, 22)
    oled.text('PS =', 0, 42)
    oled.text(ancho_ms, 40, 42)
    oled.text('ms', 76, 42)

    oled.show()
    oled.fill(0)
