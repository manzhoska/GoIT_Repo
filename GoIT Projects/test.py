from datetime import datetime, timedelta

def string_to_date(date_string):
    try:
        return datetime.strptime(date_string, "%Y-%m-%d").date()
    except ValueError:
        return datetime.strptime(date_string, "%Y.%m.%d").date()

def date_to_string(date):
    date_str = date.strftime("%Y, %m, %d")
    return date_str

def prepare_user_list(user_data):
    for user in user_data:
        birthday_obj = string_to_date(user["birthday"])
        user["birthday"] = birthday_obj
    return user_data

def find_next_weekday(start_date, weekday):
    days_ahead = start_date.weekday() - weekday
    print("days ahead: ", days_ahead)
    if days_ahead <= 0:
        days_ahead += 7
        return start_date + timedelta(days=days_ahead)
    else:
        days_ahead += 1
        return start_date + timedelta(days=days_ahead)



users = [
    {"name": "Bill Gates", "birthday": "1955.3.25"},
    {"name": "Steve Jobs", "birthday": "1955.3.21"},
    {"name": "Jinny Lee", "birthday": "1956.3.22"},
    {"name": "Sarah Lee", "birthday": "1957.3.23"},
    {"name": "Jonny Lee", "birthday": "1958.3.22"},
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

# prepare_user_list(users)

start_date = string_to_date("2020-01-01")  # Перетворення рядка на дату
# next_monday = find_next_weekday(start_date, 0)  # Знайти наступний понеділок
# print(next_monday)
next_friday = find_next_weekday(start_date, 4)  # Знайти наступну п'ятницю
print(next_friday)
