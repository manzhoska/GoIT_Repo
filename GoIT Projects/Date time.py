from datetime import datetime, timedelta, timezone
from time import time, sleep, ctime, localtime, gmtime


current_date = datetime.now()
print(current_date.year)
print(current_date.month)
print(current_date.weekday())
print(current_date.day)
print(current_date.hour)
print(current_date.minute)
print(current_date.second)
print(current_date.microsecond)
print(current_date.tzinfo)
print(current_date.date())
print(current_date.time())

date_and_time = datetime.combine(current_date.date(), current_date.time())
print(date_and_time)

#створення обʼєкта дати
specific_date = datetime(year=2026, month=5, day=6)
print(specific_date)
specific_date = datetime(year=2026, month=5, day=6, hour=9, minute = 8, second = 1)
print(specific_date)


# порівняння часу
datetime1 = datetime(2026, 3, 14, 12, 0)
datetime2 = datetime(2026, 3, 15, 12, 0)

time_delta = datetime2 - datetime1
print("Time_delta is: ", time_delta)

future_date = datetime.now() + timedelta(days=5)
print("Future date: ", future_date)
other_future_date = datetime(year=2026, month=5,day = 2)
print(other_future_date + timedelta(days=30))
print(datetime1 == datetime2)
print(datetime1 <= datetime2)
print(datetime1 != datetime2)
next_date = future_date - other_future_date
print("Days count left: ", next_date.days)

# кількість днів між двома датами за порядковим номером
difference = other_future_date.toordinal() - future_date.toordinal()
print(f"кількість днів між двома датами за порядковим номером: {future_date} та {other_future_date} ", other_future_date.toordinal(), future_date.toordinal(), f" = {difference}")






#  timestamp (часова мітка) використовується для вказівки конкретного моменту в часі
# зазвичай представляється як кількість секунд (або мілісекунд/мікросекунд у деяких системах)
#  з певної початкової дати, найчастіше з 1 січня 1970 року в UTC, це часовий пояс Гринвіча. 

time_stamp = datetime.timestamp(current_date)
print("timestamp поточного часу: ",time_stamp)

some_timestamp = 9328570088
timestamp_to_date = datetime.fromtimestamp(some_timestamp)
print(f"Переведення timestamp {some_timestamp} в дату: ",timestamp_to_date)
zero_day = datetime.fromtimestamp(0)
print("Starting day timestamp: ", zero_day)
# strftime перетворення об'єктів datetime у рядок
formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted date and time: ", formatted_date)
print("Formatted date only: ", current_date.strftime("%A, %B'%y"))
print("Formatted time only: ", current_date.strftime("%I:%M %p"))
print("Formatted date only: ", current_date.strftime("%d.%m.%Y"))

# strptime перетворення рядків у об'єкти datetime із визначеним форматом
date_string = "2026.08.01"

datetime_object = datetime.strptime(date_string, "%Y.%m.%d")
print(datetime_object)


# ISO format
print(current_date.isoformat())


# Timezone 
# для цього треба імпортувати timezone

local_now = datetime.now()
utc_now = datetime.now(timezone.utc)

print(local_now)
print(utc_now)

#зсув часового пояса та часові зони

utc_shifted_time = utc_now.astimezone(timezone(timedelta(hours=-5)))
print(utc_shifted_time)


local_timezone = timezone(timedelta(hours=2))
local_time = datetime(year=2026, month=5, day=3, hour=8, minute=55, second = 30, tzinfo=local_timezone)
print (local_time)
# конвертація локального часу в  UTC

utc_time = local_time.astimezone(timezone.utc)
print(utc_time)


# Час
current_time = time()
print("current_time from time module: ", current_time)
readable_time = ctime(current_time)
print("readable_time from time module: ", readable_time)
local_time = localtime(current_time)
print("local_time presentation: ", local_time)
gm_time = gmtime(current_time)
print("gmtime presentation in UTC: ", gm_time)

print("\nPause start")
sleep(5)
print("Pause end\n")


# Counter

start_time = time.perf_counter()
print(start_time)

# Виконуємо якусь операцію
for _ in range():
    pass  # Просто проходить цикл мільйон разів

end_time = time.perf_counter()
print(end_time)

print("execution time: ", end_time - start_time)



