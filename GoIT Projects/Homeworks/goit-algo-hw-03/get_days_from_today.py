from datetime import datetime

def get_days_from_today(date):
    # processing input date in case of invalid format
    try:
        date_obj = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        return "Please use date format: YYYY-MM-DD"

    # main calculation:
    current_date = datetime.today()
    diff_date = current_date.date() - date_obj.date()
    return diff_date.days

#showing the result of function having input date set directly:
print(get_days_from_today('2021-10-09'))