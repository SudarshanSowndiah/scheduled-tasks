import pandas
import datetime as dt
import random
import smtplib
import os

LETTER_1 = "letter_templates/letter_1.txt"
LETTER_2 = "letter_templates/letter_2.txt"
LETTER_3 = "letter_templates/letter_3.txt"
WISHING_LETTERS = "wishes_letters"
PLACEHOLDER = "[NAME]"
myEmail = os.environ.get("sudarshan111999@gmail.com")
myPwd = os.environ.get("eralnxefgrikowum")


now = dt.datetime.now()
today_month = now.month
today_day = now.day
today = (today_month, today_day)

data = pandas.read_csv("birthdays.csv")
birthday_dict = {(row.month,row.day): [row["name"], row["email"]] for (index, row) in data.iterrows()}

letters = [LETTER_1, LETTER_2, LETTER_3]
choosen_letter = random.choice(letters)

for bday in birthday_dict:
    if today == bday:
        with open(choosen_letter, mode="r") as wish_letter:
            letter_content = wish_letter.read()    
            update_letter = letter_content.replace(PLACEHOLDER, birthday_dict[bday][0])
            
            with open(f"{WISHING_LETTERS}/Birthday_wish_for_{birthday_dict[bday][0]}", mode="w") as birthday_wish:
                birthday_wish.write(update_letter)

            with open(f"{WISHING_LETTERS}/Birthday_wish_for_{birthday_dict[bday][0]}", mode="r") as for_email:
                wishing_card = for_email.read()
            
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=myEmail, password=myPwd)
                connection.sendmail(
                    from_addr=myEmail,
                    to_addrs=f"{birthday_dict[bday][1]}",
                    msg=f"Subject: HAPPY BIRTHDAY!!!\n\n{wishing_card}"
                )
