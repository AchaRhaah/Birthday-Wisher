import datetime as dt
import pandas
import random
import smtplib

data = pandas.read_csv('birthdays.csv')
data_dict = data.to_dict()

MY_EMAIL = "bettybertha033@gmail.com"
PSSSWORD = "bbertha2001"

today = dt.datetime.now()
today_tuple = (today.month, today.day)

birthdays_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_template/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        content = letter_file.read()
        birthday_letter = content.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PSSSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=birthday_person['email'],
                            msg=f"Subject:Happy Birthday!!!\n\n{birthday_letter}")
