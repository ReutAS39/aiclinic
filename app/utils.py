import datetime
import time
from datetime import timedelta, time

# """Генерирует список рабочих часов с заданным интервалом"""
#     working_hours = []
#     current_time = datetime.strptime(f"{start_hour}:00", "%H:%M")
#     end_time = datetime.strptime(f"{end_hour}:00", "%H:%M")
#
#     while current_time & lt;= end_time:
#         working_hours.append(current_time.strftime("%H:%M"))
#         current_time += timedelta(minutes=step_minutes)
#
#     return working_hours[:-1]


def freq(frequency, day_duration=14, start_hour=8):
    chunk = day_duration / (frequency-1)
    # print(chunk)
    # star_hour = 3
    # print(datetime.datetime.strptime(f"{start_hour}:00", "%H:%M"))
    # print(datetime.datetime.strptime(f"{start_hour}:00", "%H:%M"))
    current_time = datetime.datetime.strptime(f"{start_hour}:00", "%H:%M")


    # print([{i, (current_time+datetime.timedelta(hours=t*chunk)).strftime('%H:%M')} for i, t in enumerate(range(frequency), start=1)])
    # print([{i, (current_time+datetime.timedelta(hours=t*chunk))} for i, t in enumerate(range(frequency), start=1)])




    return {i: (current_time+datetime.timedelta(hours=t*chunk)).strftime('%H:%M') for i, t in enumerate(range(frequency), start=1)}
    # return [{i: t*chunk + start_hour} for i, t in enumerate(range(frequency), start=1)]


