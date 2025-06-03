# Keeping track of screen time across devices, simple use of datetime.
import datetime

file = input("Filename: ")
start_date_str = input("Starting date: ")
days = int(input("How many days: "))
print("Please type in screen time in minutes on each day (TV computer mobile): ")

start_date = datetime.datetime.strptime(start_date_str, "%d.%m.%Y").date()

screen_time_data = []

for i in range(days):
    current_date = start_date + datetime.timedelta(days=i)
    date_str = current_date.strftime("%d.%m.%Y")
    entry = input(f"Screen time {date_str}: ")
    screen_time_data.append((date_str, entry.strip()))

end_date = start_date + datetime.timedelta(days=len(screen_time_data) -1)
total_minutes = 0

lines = []

for date_str, entry in screen_time_data:
    minutes = sum(int(x) for x in entry.split())
    total_minutes += minutes
    formatted_entry = entry.replace(" ", "/")
    lines.append(f"{date_str}: {formatted_entry}")

average_minutes = total_minutes / len(screen_time_data)

with open (file, "w") as f:
    f.write(f"Time period: {start_date.strftime('%d.%m.%Y')}-{end_date.strftime('%d.%m.%Y')}\n")
    f.write(f"Total minutes: {total_minutes}\n")
    f.write(f"Average minutes: {average_minutes:.1f}\n")
    for line in lines:
        f.write(line + "\n")

print(f"Data stored in file {file}")
