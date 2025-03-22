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
    day_schedule = 0

    def __init__(self, frequency: int, upcoming_period: int = 1, test=None):
        self.frequency = frequency
        self.upcoming_period = upcoming_period
        self.test=test

    def get_day_schedule(self):
        chunk = self.day_duration / (self.frequency - 1)
        dawn = DT.datetime.strptime(f"{self.start_hour}:00", "%H:%M")
        day_schedule = {i: (dawn + DT.timedelta(minutes=round_to_15(round(t * chunk * 60)))).strftime('%H:%M') for i, t in
                enumerate(range(self.frequency), start=1)}

        return day_schedule

    def get_next_taking(self):
        now = DT.datetime.now()
        zzz = {}

        for doctors_stuff, sh in self.test.items():
            for n, t in sh.items():
                if (DT.datetime.strptime(t, "%H:%M").time().hour - now.time().hour) in (0, self.upcoming_period):
                    zzz[doctors_stuff] = t

        return zzz


