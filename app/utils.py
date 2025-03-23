import datetime as DT
from .config import UPCOMING_PERIOD


round_to_15 = lambda x: round(x / 15) * 15


class ScheduleManager:
    day_duration = 14
    start_hour = 8

    def __init__(self, frequency: int = None, test=None, upcoming_period: int = UPCOMING_PERIOD):
        self.frequency = frequency
        self.upcoming_period = upcoming_period
        self.test = test

    @classmethod
    async def get_day_schedule(cls, frequency: int):
        chunk = cls.day_duration / (frequency - 1)
        start_time = DT.datetime.strptime(f"{cls.start_hour}:00", "%H:%M")
        day_schedule = {i: (start_time + DT.timedelta(minutes=round_to_15(round(t * chunk * 60)))).strftime('%H:%M')
                        for i, t in enumerate(range(frequency), start=1)}

        return day_schedule

    def get_next_taking(self):
        now = DT.datetime.now()
        next_taking = {}

        for doctors_stuff, sh in self.test.items():
            for n, t in sh.items():
                if (DT.datetime.strptime(t, "%H:%M").time().hour - now.time().hour) in (0, self.upcoming_period):
                    next_taking[doctors_stuff] = t

        return next_taking

