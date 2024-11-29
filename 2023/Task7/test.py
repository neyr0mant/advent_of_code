from datetime import datetime
res_1 = '2024-10-17T17:22:09'
res_2 = '2024-10-17T17:22:26'
list_date_1 = res_1.replace("T", "-").replace(":", "-").split("-")
year, month, day, hour, mint, sec = [int(i) for i in list_date_1]
date_1 = datetime(year, month, day, hour,mint, sec)
list_date_2 = res_2.replace("T", "-").replace(":", "-").split("-")
year, month, day, hour, mint, sec = [int(i) for i in list_date_2]
date_2 = datetime(year, month, day, hour,mint, sec)
res3 = date_2 - date_1
print()

def assert_date(date_1, date_2):
    list_date_1 = date_1.replace("T", "-").replace(":", "-").split("-")
    year_1, month_1, day_1, hour_1, mint_1, sec_1 = [int(i) for i in list_date_1]
    date_1 = datetime(year_1, month_1, day_1, hour_1, mint_1, sec_1)
    list_date_2 = date_2.replace("T", "-").replace(":", "-").split("-")
    year_2, month_2, day_2, hour_2, mint_2, sec_2 = [int(i) for i in list_date_2]
    date_2 = datetime(year_2, month_2, day_2, hour_2, mint_2, sec_2)
    date_old = date_1 if date_1 <= date_2 else date_2
    date_new = date_2 if date_2 >= date_1 else date_1
    delta_sec = date_new - date_old
    return delta_sec.seconds

print(assert_date(res_2, res_1))