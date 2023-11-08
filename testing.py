import datetime as dt

today = str(dt.date.today())

today_list = today.split("-")

year = today_list[0]
month = today_list[1]
day = today_list[2]

print ( year, month, day )
