## Тестовое задание

Доктор Айболит заметил, что каждый день
прописывает своим пациентам-зверям таблетки 
в качестве лечения. Однако звери ведут достаточно
активный образ жизни и часто забывают 
о своевременном приёме таблеток. Доктор Айболит
долго размышлял, как решить эту проблему, 
и наконец решил создать мобильное приложение 
(да-да, в нашем лесу уже есть такие технологии),
которое будет напоминать его пациентам о приёме
лекарств  
Итак, первым делом доктор подтянул свои знания 
в области backend-технологий и составил список
предварительных требований к сервису, который
необходимо разработать:
Все лекарства принимаются только в течение дня, 
а значит, ночью никаких приемов таблеток 
не должно быть. Подумав еще немного, доктор
зафиксировал, что днем будет считаться интервал
времени с 8:00 утра до 22:00 вечера
В списке таблеток, которые он назначает,
встречаются разные варианты по периодичности
приема: от одного раза в день до ежечасного приёма
Среди таблеток есть такие, которые следует
принимать на протяжении определенного периода
(например, в течение двух недель), а есть и такие,
которые следует принимать постоянно
Минуты во всех рассчитанных временных метках 
он решил делать кратными 15 (то есть, если время
приема рассчиталось как 17:07, то мобильное
приложение должно округлять его до 17:15)
Вследствие этих требований доктор запланировал,
что его HTTP-сервис должен поддерживать
следующие HTTP-роуты:
```python
POST /schedule
```
+ ***Наименование лекарства;***
+ ***Периодичность приёмов;***
+ ***Продолжительность лечения;***
+ ***Идентификатор пользователя (у каждого зверя есть 
медицинский полис, будем считать, что его номер это 
и есть идентификатор пользователя).***

В ответ роут должен возвращать идентификатор созданного
расписания из базы данных
```python
GET /schedules?user_id=
```
Возвращает список идентификаторов существующих
расписаний для указанного пользователя

```python
GET /schedule?user_id=&schedule_id=
```

Возвращает данные о выбранном расписании с рассчитанным
графиком приёмов на день

```python
GET /next_takings?user_id=
```
Возвращает данные о таблетках, которые необходимо принять 
в ближайшие период (например, в ближайший час). Период
времени задается через параметры конфигурации сервиса

Звери не знают и не могут угадать номера
медицинских полисов (user_id) друг друга, знают
только свой, а поэтому, дополнительная
аутентификация/авторизация не требуется


## Установка

1. Клонируйте репозиторий:

   ```bash
   git clone https://github.com/ReutAS39/aiclinic.git
   ```

2. Перейдите в директорию проекта:

   ```bash
   cd aiclinic
   ```

3. Создайте и активируйте виртуальное окружение:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Для Windows: venv\Scripts\activate
   ```

4. Установите зависимости:

   ```bash
   pip install -r requirements.txt
   ```


5. Запуск приложения: 

   ```bash
   uvicorn app.main:app
   ```
