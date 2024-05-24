from datetime import date

# Get the current day's date
current_date = date.today()

# Get the day of the week (Monday, Tuesday, etc.)
day_of_week = current_date.strftime('%A')

# Print the current date and day of the week
time = f"{day_of_week} : {current_date}"
print(time)