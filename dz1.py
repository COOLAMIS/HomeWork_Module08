from datetime import datetime, timedelta
from collections import defaultdict


users = [{"name": "Vasya", "birthday": datetime(1989, 8, 3)},
         {"name": "Misha", "birthday": datetime(1991, 7, 29)},
         {"name": "Pasha", "birthday": datetime(1992, 7, 30)},
         {"name": "Jora", "birthday": datetime(1992, 8, 4)}
        ]

def get_period() -> tuple[datetime.date, datetime.date]:
    current_date = datetime.now()
    start_period = current_date + timedelta(days = 5 - current_date.weekday())
    return start_period.date(), (start_period + timedelta(6)).date()

def check_users(list_users):
    list_congratulation = defaultdict(list)
    current_year = datetime.now().year
    for i in list_users:
        bd = i["birthday"]
        bd = bd.date()
        bd = bd.replace(year = current_year)
        start, end = get_period()
        if start <= bd <= end:        
            if bd.weekday() in (5,6):
                list_congratulation["Monday"].append(i["name"])
            else:
                list_congratulation[bd.strftime("%A")].append(i["name"])
    return list_congratulation
        
print(check_users(users))

