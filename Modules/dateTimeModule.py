from datetime import date, datetime

today_date = date.today()
print(today_date)

current_time = datetime.now()
print(current_time)

current_only_time = current_time.time()
print(current_only_time)