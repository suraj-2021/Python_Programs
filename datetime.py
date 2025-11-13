from datetime import datetime, timedelta

now = datetime.now()
print("Current date and time:", now)

days_to_add = 5
future_date = now + timedelta(days=days_to_add)
print(f"Date after {days_to_add} days:", future_date)

days_to_subtract = 3
past_date = now - timedelta(days=days_to_subtract)
print(f"Date before {days_to_subtract} days:", past_date)

date1 = datetime(2025, 11, 10)
date2 = datetime(2025, 11, 15)
difference = date2 - date1
print("Difference between dates:", difference.days, "days")
