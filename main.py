
"""
my_email = "deepaksbisht54321@gmail.com"
password = "bjfd ndhw zqxk xbzs"
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls() # to secure & encrypt our message
connection.login(user=my_email, password=password)
connection.sendmail(
    from_addr=my_email,
    to_addrs="nonormal12345@yahoo.com",
    msg="Subject:hello\n\nThis is the body of my email")
connection.close()

import datetime as dt  # datetime module:tell us current date and time
time = dt.datetime.now()  # tell us current date and time
year = time.year  # tell us current year
month = time.month  # tell us current month
day = time.day  # tell us current day
hour = time.hour  # tell us current hour
min = time.minute  # tell us current minute
sec = time.second  # tell us current second
day_of_week = time.weekday()  # tell us current day of week eg:0-monday,1-tuesday,....6-sunday
date_of_birth=dt.datetime(year=2007, month=9, day=2)
if hour == 10:
    print(f"happy birthday {hour}")
print(time)
print(f"date= {day}:{month}:{year}")
print(f"time= {hour}:{min}:{sec}")
print(date_of_birth)
"""
import random
import smtplib
import datetime as dt  # datetime module:tell us current date and time
with open("quotes.txt", "r") as file:  # open quotes.txt in read mode
    data = file.readlines()  # Read all lines from the file and store them in a list
# print(data)  # Print the list to check the content
# To remove newline characters (\n), you can use list comprehension:
data = [line.strip() for line in data]  # line.strip() removes any leading and trailing whitespace, including newline characters
select = random.choice(data)  # randomly select any list of element from data list
# print(select)  # print randomly select any list of element from data list
# daytime
time = dt.datetime.now()
day_of_week = time.weekday()  # tell us current day of week eg:0-monday,1-tuesday,....6-sunday
if day_of_week == 2:
    my_email = "deepaksbisht54321@gmail.com"
    password = "bjfd fuik ghtr xbzs"
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()  # to secure & encrypt our message
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="deepaksbisht54321@gmail.com",
        msg=f"Subject:Monday Motivation\n\n{select}")
    connection.close()




