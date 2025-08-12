import smtplib
import random 
import datetime as dt

email = ""
app_password = ""

with open("quotes.txt", "r") as quotes_data:
    lines = quotes_data.read().splitlines()

now = dt.datetime.now()
day_of_week = now.weekday()

if day_of_week == 0:
    with smtplib.SMTP("smtp.gmail.com") as connect:
        connect.starttls()
        connect.login(user=email, password=app_password)
        connect.sendmail(
            from_addr=email, 
            to_addrs="", 
            msg=f"Subject: Monday Motivation\n\n{random.choice(lines)}")

