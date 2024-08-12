#Dates
from datetime import datetime                   #Crear fecha actual

now = datetime.now()

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)


timestamp= now.timestamp()                      #Representación numérica de un momento específico en el tiempo
print(timestamp)


def print_dates(dates):
    print(dates.year)
    print(dates.month)
    print(dates.day)
    print(dates.hour)
    print(dates.minute)
    print(dates.second)

print_dates(now)

year_2024 = datetime(2024, 8, 12)           #Construir fecha
print(year_2024)


from datetime import time                               #Representar tiempo

current_time = time(21, 6, 0)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)



from datetime import date                               #Representar una fecha

current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)


current_date = date(2024, 5, 21)

print(current_date.year)
print(current_date.month)
print(current_date.day)

#Modificar datos en las fechas 
current_date = date(current_date.year, current_date.month + 2, current_date.day)
print(current_date)


diff = year_2024 - now
print(diff)


from datetime import timedelta

start_time_delta = timedelta(200, 100, 100, weeks = 10)
end_time_delta = timedelta(100, 50, 80, weeks = 23)

print(start_time_delta - end_time_delta)