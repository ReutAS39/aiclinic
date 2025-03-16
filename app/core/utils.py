# import datetime
# from datetime import timedelta
#
#
# def generate_working_hours(cls, start_hour=8, end_hour=22, step_minutes=30):
#     """Генерирует список рабочих часов с заданным интервалом"""
#     working_hours = []
#     current_time = datetime.strptime(f"{start_hour}:00", "%H:%M")
#     end_time = datetime.strptime(f"{end_hour}:00", "%H:%M")
#
#     while current_time & lt;= end_time:
#         working_hours.append(current_time.strftime("%H:%M"))
#         current_time += timedelta(minutes=step_minutes)
#
#     return working_hours[:-1]