from app.api.schemas import CreateSchedule


def create_schedule(schedule: CreateSchedule):
    schedule = schedule.model_dump()
    return {
        "success": True,
        "schedule": schedule
    }
