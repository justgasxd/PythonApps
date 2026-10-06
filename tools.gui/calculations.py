# calculations.py
from datetime import datetime

def calculate_average(grade1, grade2, grade3):
    """Arvutab hinnete keskmise"""
    return (grade1 + grade2 + grade3) / 3

def calculate_work_time(start_time, end_time):
    """Arvutab tööaja algus- ja lõpukellaaja põhjal"""
    start = datetime.strptime(start_time, '%H:%M')
    end = datetime.strptime(end_time, '%H:%M')

    if end < start:
        start, end = end, start

    difference = end - start
    total_minutes = int(difference.total_seconds() // 60)

    hours = total_minutes // 60
    minutes = total_minutes % 60

    return hours, minutes

def convert_temperature(temperature, direction):
    """Teisendab temperatuuri C -> F ja F -> C"""
    if direction == 'C_TO_F':
        return temperature * 9 / 5 + 32 # F
    return (temperature -32) * 5 /9 # C
