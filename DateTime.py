
# Working with date and time in python
import datetime

# to use module in python, we create the module object
# objName = module.module's_method() or
# objName = module.module's_method(args)

# some datetime module method: .date(YY, MM, DD), .today() with the .date(), .time(HH,MM,SS), .datetime(HH, MM, SS YY, MM, DD), .datetime.now(), .strftime(datetime format specifiers)

date = datetime.date(2025, 4, 19) # date object
# obj to use system date
today = datetime.date.today()

#time obj
time = datetime.time(10, 20, 50)
# obj to use sys time
now = datetime.datetime.now()
now = now.strftime("Time => %H:%M:%S Date => %m-%d-%Y")
#print(now)

# Exercise 1
target_datetime = datetime.datetime(2025, 4, 19, 12, 00, 30)
current_datetime = datetime.datetime.now()

if target_datetime < current_datetime:
    print("Target date has passed")
else:
    print("Target date has NOT passed")



