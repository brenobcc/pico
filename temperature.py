from machine import ADC# type: ignore
from time import sleep

def calculateInternalTemp(sensor_temp):
    reading = sensor_temp.read_u16()

    conversion_constant = 3.3 / 65535
    
    temp_ref = 27 #ºC
    volt_ref = 0.706 #V
    
    temp_coef = 0.001721 # dV/dT

    voltage = conversion_constant * reading
    temperature = temp_ref - (voltage - volt_ref) / temp_coef
    
    return temperature

sensor_temp = ADC(4)

while True:
    temp = calculateInternalTemp(sensor_temp)
    
    print(f"Temperatura Raspberry: {temp}")
    
    sleep(1)