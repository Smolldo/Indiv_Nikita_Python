#  len() - длина последовательности

a = 'sfgsjfdgfxg'

b = {
    1: 1,
    2: 2
}

# c = 123

print(len(b))


#  min() max()

c = [1,2,3,4,5,6,7,8,9]

d = 'abcdefghijklmo'

print(min(d))
print(max(d))


# abs() - модуль числа

print(abs(2))
print(abs(-2))


# sum()

e = [1,2,3,4,5,6]

# f = 123

print(sum(e))


from datetime import date, time, datetime, timedelta


today = date.today() # yyyy-mm-dd

print(today)

# print(f'Year: {today.year}')
# print(f'Month: {today.month}')

lunch_time = time(13, 30, 00)
# print(f'Lanch time at: {lunch_time}')

now = datetime.now()
# print(now)
# print(now.date())

duration = timedelta(weeks=10, minutes=68)
# print(duration)

future_date = now + duration
# print(future_date)


# strftime() - string formating time

d = date(2025, 2, 22)

t = time(12,55,32)

formatted_date = d.strftime('%B %d, %Y')
formatted_time = t.strftime('%H hours %M minutes %S seconds')

# print(formatted_date)
# print(formatted_time)
import time

start_time = time.perf_counter()

# for i in range(100000000):
#     pass

finish_time = time.perf_counter()

execution_time = finish_time - start_time
# print(execution_time)

utc_time = time.gmtime()
print("UTC Time:", time.strftime("%Y-%m-%d %H:%M:%S", utc_time))

local_time = time.localtime()
print("Local Time:", time.strftime("%Y-%m-%d %H:%M:%S", local_time))
