from datetime import datetime, timedelta
from app.config import settings


def get_mul_15(x):
    return round(x / 15) * 15


def get_minutes(obj):
    return obj.time().hour*60 + obj.time().minute


class ScheduleManager:
    day_duration = 14
    start_hour = 8
    now = datetime.now()

    @classmethod
    def get_day_schedule(cls, frequency: int):
        start_time = datetime.strptime(f"{cls.start_hour}:00", "%H:%M")
        if frequency > 1:
            chunk = cls.day_duration / (frequency - 1)
            day_schedule = {i: (start_time + timedelta(minutes=get_mul_15(t * chunk * 60))).strftime('%H:%M')
                            for i, t in enumerate(range(frequency), start=1)}
            return day_schedule
        return {"1": (start_time + timedelta(hours=cls.day_duration/2)).strftime('%H:%M')}

    @classmethod
    def get_next_takings(cls, all_schedules: dict, upcoming_period: int = settings.UPCOMING_PERIOD):
        now = datetime.now()
        next_takings = {}
        for doctors_stuff, periods_dict in all_schedules.items():
            for _, t in periods_dict.items():
                if 0 < (get_minutes(datetime.strptime(t, "%H:%M")) - get_minutes(now)) < upcoming_period:
                    next_takings[doctors_stuff] = t
                    break
        return next_takings
