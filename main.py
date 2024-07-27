import pandas
import datetime
import random
import smtplib

# email info
my_email = "negartoorany283@gmail.com"
my_password = "fooled ya!"
# Reading from the birthday.csv
read_csv = pandas.read_csv("birthdays.csv")
birth_info = pandas.DataFrame(read_csv)
name = birth_info["name"]

# Getting the date
dt = datetime.datetime.now()
today_month = dt.month
today_year = dt.year
today = dt.day
# checking if the date match
user_year = birth_info["year"]
user_month = birth_info["month"]
user_day = birth_info["day"]
# finding the birthday person
user = birth_info[
    (birth_info["year"] == today_year) & (birth_info["month"] == today_month) & (birth_info["day"] == today)]
birthday_person = user["name"].values[0]

# Reading the letters
random_int = random.randint(1, 3)
with open(f"letter_templates/letter_{random_int}.txt") as file:
    read_file = file.read()
    ready_email = read_file.replace("[NAME]", birthday_person)
# sending the Email
user_email = user["email"].values[0]
with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email, to_addrs=user_email, msg=f"Subject:Happy birthday!\n\n{ready_email}")
