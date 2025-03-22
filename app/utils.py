import datetime as DT

# def freq(frequency, day_duration=14, start_hour=8):
#     chunk = day_duration / (frequency-1)
#     dawn = DT.datetime.strptime(f"{start_hour}:00", "%H:%M")
#     print(dawn)
#
#
#     # return {i: (dawn+DT.timedelta(hours=t*chunk)).strftime('%H:%M') for i, t in enumerate(range(frequency), start=1)}
#     return {i: (dawn+DT.timedelta(minutes=round_to_15(round(t*chunk*60)))).strftime('%H:%M') for i, t in enumerate(range(frequency), start=1)}
#

round_to_15 = lambda x: round(x / 15) * 15


class ScheduleManager:
    day_duration = 14
    start_hour = 8

    def __init__(self, frequency):
        self.frequency = frequency

    def get_day_schedule(self):
        chunk = self.day_duration / (self.frequency - 1)
        dawn = DT.datetime.strptime(f"{self.start_hour}:00", "%H:%M")

        return {i: (dawn + DT.timedelta(minutes=round_to_15(round(t * chunk * 60)))).strftime('%H:%M') for i, t in
                enumerate(range(self.frequency), start=1)}
