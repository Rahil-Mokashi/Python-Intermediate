##################### Extra Hard Starting Project ######################

import pandas
import smtplib
import datetime as dt
import random

email = ""
app_password = ""


# 1. Update the birthdays.csv
birthday_data = pandas.read_csv("birthdays.csv")

# 2. Check if today matches a birthday in the birthdays.csv

now = dt.datetime.now()
current_month = now.month
current_day = now.day

birthday_row = birthday_data[(birthday_data['month']==current_month) & (birthday_data['day']==current_day)]

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if not birthday_row.empty:    
    
    letters = ["./letter_templates/letter_1.txt", './letter_templates/letter_2.txt', './letter_templates/letter_3.txt']

    # 4. Send the letter generated in step 3 to that person's email address.

    with smtplib.SMTP("smtp.gmail.com") as birthday_mail:
        birthday_mail.starttls()
        birthday_mail.login(user=email, password=app_password)
        
        for _, row in birthday_row.iterrows():
            birthday_name = row['name']
            birthday_email = row['email']
            
            birthday_letter_path = random.choice(letters)

            with open(birthday_letter_path, 'r') as file:
                filedata = file.read()
        
            message = filedata.replace('[NAME]', birthday_name)
        
            birthday_mail.sendmail(from_addr=email, to_addrs=birthday_row['email'], msg=f"Subject: Happy Birthday! \n\n{message}")
        
            print(f"✅ Email sent to {birthday_name} at {birthday_email}")
else:
    print("No birthdays today.")


