import datetime

d = datetime.date(2019, 2, 27)
print(d)

# yesterday = datetime.date.yesterday()
# print(yesterday)

today = datetime.date.today()
# print(today)

# print(today.year)

# print(today.weekday())
# print(today.isoweekday())

tdelta = datetime.timedelta(days=7)

print(today + tdelta)