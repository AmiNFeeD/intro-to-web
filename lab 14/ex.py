from datetime import datetime, timedelta
import time

#1 Displaying the current date and time

now = datetime.now()

formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
print("Current Date and Time:", formatted_now)

#2 Calculating the difference between two dates

today = datetime.now()

new_years_eve = datetime(today.year, 12, 31)

if today > new_years_eve:
    new_years_eve = datetime(today.year + 1, 12, 31)

time_until_new_year = new_years_eve - today

print("Days until New Year's Eve:", time_until_new_year.days)

#3 Implementing a countdown timer

def countdown_timer(seconds):
    end_time = datetime.now() + timedelta(seconds=seconds)
    while True:
        remaining = end_time - datetime.now()
        total_seconds = int(remaining.total_seconds())
        if total_seconds <= 0:
            print("Time remaining: 0 seconds")
            break

        print(f"Time remaining: {total_seconds} seconds", end="\r")
        time.sleep(1)
    print("\nTimer finished!")

countdown_timer(10)


#4 Creating a simple month calendar

def simple_month_calendar(year, month):
    current_date = datetime(year, month, 1)
    start_weekday = current_date.weekday()

    if month == 12:
        next_month = datetime(year + 1, 1, 1)
    else:
        next_month = datetime(year, month + 1, 1)
    last_day = next_month - timedelta(days=1)

    print("Mon Tue Wed Thu Fri Sat Sun")
    print("   " * start_weekday, end="")

    while current_date <= last_day:
        print(f"{current_date.day:3}", end="")
        if current_date.weekday() == 6:
            print()
        current_date += timedelta(days=1)

    print()

simple_month_calendar(2025, 5)
