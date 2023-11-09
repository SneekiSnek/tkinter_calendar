import datetime as dt

today = str(dt.date.today())

today_list = today.split("-")

year = int(today_list[0])
month = int(today_list[1])
day = int(today_list[2])

print ( year, month, day )

yday = (dt.date.toordinal(dt.date.today())) - ((year - 1) * 365.242)
print (yday)