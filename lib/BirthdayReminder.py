from datetime import datetime
from dateutil.relativedelta import relativedelta

class BirthdayReminder:
    # User-facing properties:
    #   name: string

    def __init__(self):
        self.birthday_book = {}

    def add(self, name, date):
        if name == "":
            raise Exception("Please enter valid name!")
        if date == "":
            raise Exception("Please enter valid date!")
        
        today = datetime.today()
        birthdate = datetime.strptime(date, "%d-%m-%Y")

        age = (
            today.year
            - birthdate.year
            - ((today.month, today.day) < (birthdate.month, birthdate.day))
        )

        self.birthday_book[name] = {
            "birthday": date,
            "age": age,
            "card_status": "not sent",
        }

    def update_date(self, name, date):
        self.birthday_book[name]["birthday"] = date

    def update_name(self, old_name, new_name):
        if old_name in self.birthday_book:
            self.birthday_book[new_name] = self.birthday_book.pop(old_name)

    def upcoming_birthdays(self):
        today = datetime.today()
        upcoming_bdays = []
        upcoming_30_days = []
        for blob in [today + relativedelta(days=i) for i in range(1, 30)]:
            upcoming_30_days.append(blob.strftime("%d-%m"))

        for i in self.birthday_book:
            if self.birthday_book[i]["birthday"][:5] in upcoming_30_days:
                upcoming_bdays.append(i)
        return ", ".join(upcoming_bdays)

    def send_card(self, name):
        if self.birthday_book[name]["card_status"] == "sent":
            raise Exception("Card already sent!")
        else:
            self.birthday_book[name]["card_status"] = "sent"
