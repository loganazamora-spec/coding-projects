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


def check_data(rand_temp, rand_volt, rand_curr, rand_speed):
    '''Check's data from collect_data() if it's within the ranges provided'''
    # Start with them not being safe
    temp_safe, volt_safe, curr_safe, speed_safe = False

    for sensor in sensors:
            if rand_temp in range(sensors[0]["min_safe"], sensors[0]["max_safe"]):
                temp_safe = True
            if rand_volt in range(sensors[1]["min_safe"], sensors[1]["max_safe"]):  
                volt_safe = True
            if rand_curr in range(sensors[2]["min_safe"], sensors[2]["max_safe"]):
                curr_safe = True
            if rand_speed in range(sensors[3]["min_safe"], sensors[3]["max)_safe"]):
                speed_safe = True   

    return temp_safe, volt_safe, curr_safe, speed_safe
                

def collect_data():
    ''' Simulates data collection by providing random integers and returning them '''
    rand_temp = random.randint(0, 90)
    rand_volt = random.randint(10, 16)
    rand_curr = random.randint(0, 18)
    rand_speed = random.randint(0, 320)

    return [rand_temp, rand_volt, rand_curr, rand_speed]

def append_data(data):
    '''Appends collected data to sensor_data dict'''
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
        print(f"This step's data: {data}")

        # Check if data is in safe range
        safety = check_data(rand_temp=data[0], rand_volt=data[1], rand_curr=data[2], rand_speed=data[3])
        for sensor in sensors:
            name = sensor["name"]
            print(f"{name} | {safety}")

            if safety == False:
                print(f"WARNING! {name.capitalize()} sensor received with {steps_remaining} steps remaining. ")
        

        # Append data to list
        append_data(data=data)
        

        steps_remaining -= 1

    print(f"Sensor data from all steps: {sensor_data}")

main()