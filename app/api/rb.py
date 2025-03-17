class RBSchedules:
    def __init__(self,
                 user_id: int | None = None,):

        self.user_id = user_id


    def to_dict(self) -> dict:
        data = {'user_id': self.user_id,}
        # print(data)
        # Создаем копию словаря, чтобы избежать изменения словаря во время итерации
        filtered_datas = {key: value for key, value in data.items() if value is not None}
        # print(filtered_datas)
        return filtered_datas

class RBSchedule:
    def __init__(self, schedule_id: int | None = None,
                 user_id: int | None = None,):
        self.id = schedule_id
        self.user_id = user_id


    def to_dict(self) -> dict:
        data = {'id': self.id, 'user_id': self.user_id,}
        filtered_data = {key: value for key, value in data.items() if value is not None}
        return filtered_data