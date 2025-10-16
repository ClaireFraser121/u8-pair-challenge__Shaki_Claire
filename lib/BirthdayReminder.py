from datetime import datetime

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
        # Parameters:
        #   self
        # Returns:
        #   upcoming birthdays, names, age, and card status (done/not done)
        # Side-effects
        #   none
        pass  # No code here yet

    def send_card(self, name):
        # Parameters:
        #   name: a string representing a name
        # Returns:
        #   string: "You have sent a card to {name}"
        # Side-effects
        #   add done to to the entry
        pass  # No code here yet
