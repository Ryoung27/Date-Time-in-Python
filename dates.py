import datetime

# d = datetime.date(2019, 2, 27)
# print(d)

# # yesterday = datetime.date.yesterday()
# # print(yesterday)

# today = datetime.date.today()
# # print(today)

# # print(today.year)

# # print(today.weekday())
# # print(today.isoweekday())

# tdelta = datetime.timedelta(days=7)

# print(today + tdelta)

# print(today - datetime.timedelta(days=10))

# bday = datetime.date(2019, 12, 6)

# till_birthday = bday - today

# print(till_birthday)

# today = datetime.time(9, 20, 10, 10000)
# print(today)

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print(dt_today)
print(dt_now)
print(dt_utcnow)