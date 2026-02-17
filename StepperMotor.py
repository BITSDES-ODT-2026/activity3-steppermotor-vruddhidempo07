Stepper Motor
from machine import Pin
import time

IN1 = Pin(5,Pin.OUT)
IN2 = Pin(14,Pin.OUT)
IN3 = Pin(15,Pin.OUT)
IN4 = Pin(19,Pin.OUT)

while True:
    IN1.value(1)
    IN2.value(0)
    IN3.value(0)
    IN4.value(0)
    time.sleep_ms(5)
    
    IN1.value(0)
    IN2.value(1)
    IN3.value(0)
    IN4.value(0)
    time.sleep_ms(5)
    
    IN1.value(0)s
    IN2.value(0)
    IN3.value(1)
    IN4.value(0)
    time.sleep_ms(5)
    
    IN1.value(0)
    IN2.value(0)
    IN3.value(0)
    IN4.value(1)
    time.sleep_ms(5)

Anticlockwise and Clockwise
from machine import Pin
import time

IN1 = Pin(5,Pin.OUT)
IN2 = Pin(14,Pin.OUT)
IN3 = Pin(15,Pin.OUT)
IN4 = Pin(19,Pin.OUT)

while True:
    for i in range(500):
        IN1.value(1)
        IN2.value(0)
        IN3.value(0)
        IN4.value(0)
        time.sleep_ms(5)
        
        IN1.value(0)
        IN2.value(1)
        IN3.value(0)
        IN4.value(0)
        time.sleep_ms(5)
        
        IN1.value(0)s
        IN2.value(0)
        IN3.value(1)
        IN4.value(0)
        time.sleep_ms(5)
        
        IN1.value(0)
        IN2.value(0)
        IN3.value(0)
        IN4.value(1)
        time.sleep_ms(5)
        
        IN1.value(0)
        IN2.value(0)
        IN3.value(0)
        IN4.value(1)
        time.sleep_ms(5)
        
        IN1.value(0)
        IN2.value(0)
        IN3.value(1)
        IN4.value(0)
        time.sleep_ms(5)
        
        IN1.value(0)
        IN2.value(1)
        IN3.value(0)
        IN4.value(0)
        time.sleep_ms(5)
        
        IN1.value(1)
        IN2.value(0)
        IN3.value(0)
        IN4.value(0)
        time.sleep_ms(5)

  Anticlockwise and Clockwise using LIST
from machine import Pin
import time

in1 = Pin(5,Pin.OUT)
in2 = Pin(14,Pin.OUT)
in3 = Pin(15,Pin.OUT)
in4 = Pin(19,Pin.OUT)

lalu = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
r_lalu = [[0,0,0,1],[0,0,1,0],[0,1,0,0],[1,0,0,0]]

while True:
    for k in range(500):
        for i in lalu:
            in1.value(i[0])
            in2.value(i[1])
            in3.value(i[2])
            in4.value(i[3])
            time.sleep_ms(5)
        
    for h in range(500):
        for g in r_lalu:
            in1.value(g[0])
            in2.value(g[1])
            in3.value(g[2])
            in4.value(g[3])
            time.sleep_ms(5)
