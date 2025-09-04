
import datetime

def dt_now_demo():
    #Current date & time
    now = datetime.datetime.now()
    print("Now:", now)

def dt_today_demo():
    #Today's date
    today = datetime.date.today()
    print("Today:", today)

def dt_create_demo():
    #Create a specific datetime
    d = datetime.datetime(2025, 1, 1, 9, 30, 0)
    print("Created:", d)

def dt_format_demo():
    #Format datetime with strftime
    now = datetime.datetime.now()
    out = now.strftime("%d-%b-%Y %I:%M %p")
    print("Formatted:", out)


dt_now_demo()
dt_today_demo()
dt_create_demo()
dt_format_demo()
