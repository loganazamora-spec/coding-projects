'''Python program that simulates a data pipeline for a small autonomous rover. 
The rover has four sensors. The program runs a simulation over 10 time steps, 
collects data from each sensor at every step, stores it, and produces a final 
diagnostic report.'''

import random

sensor_data = {} 

# Sensor information
sensors = [
    {"id": "S001", "name": "temperature", "unit": "°C", "min_safe": 0, "max_safe": 80},
    {"id": "S002", "name": "battery_voltage", "unit": "V", "min_safe": 11.0, "max_safe": 14.8},
    {"id": "S003", "name": "motor_current", "unit": "A", "min_safe": 0, "max_safe": 15},
    {"id": "S004", "name": "wheel_speed", "unit": "RPM", "min_safe": 0, "max_safe": 300},
]



def collect_data():
    ''' Simulates data collection by providing random integers and returning them '''
    rand_temp = random.randint(0, 90)
    rand_volt = random.randint(10, 16)
    rand_curr = random.randint(0, 18)
    rand_speed = random.randint(0, 320)

    if ...:
        return [rand_temp, rand_volt, rand_curr, rand_speed]

def append_data(data):
    ''' Appends collected data to sensors_data dict'''
    for sensor in sensors:
        sens_id = sensor["id"]
        sensor_data[sens_id] = data
         
    return sensor_data

def main():
    steps_remaining = 10

    while steps_remaining > 0:
        # Run for 10 steps

        # Collect data from each sensor
        data = collect_data()
        print(data)

        # Append data to list
        append_data(data=data)
        
        

        steps_remaining -= 1

    print(sensor_data)

main()