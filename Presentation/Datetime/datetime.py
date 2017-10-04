import datetime

# Simple naive date requires year, month, day
mydate = datetime.date(1943, 3, 13)  

# Prints date as year, month, & day
print(mydate)

# Prints day of the week for the given date using strftime
print(mydate.strftime("%A"))

# Shows current date
today = datetime.date.today()
print(today)

# Time deltas calculate the difference between two dates or times.

# Duration of 7 days
time_delta = datetime.timedelta(days=7)

# Print date one week from now
print(today + time_delta)

# Print date from one week ago
print(today - time_delta)

# Time delta used for countdown
thanksgiving = datetime.date(2017, 11, 23)
until_thanksgiving = thanksgiving - today

print until_thanksgiving
print until_thanksgiving.days
print until_thanksgiving.total_seconds()
