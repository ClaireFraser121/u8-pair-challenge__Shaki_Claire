from datetime import datetime


class BirthdayReminder:
    # User-facing properties:
    #   name: string

    def __init__(self):
        self.birthday_book = {}

    def add(self, name, date):
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

    #     def calculateAge(birthDate):
    #         today = date.today()
    #         age = today.year - birthDate.year -
    #         ((today.month, today.day) <
    #         (birthDate.month, birthDate.day))

    #         return age

    # # Driver code
    # print(calculateAge(date(1997, 2, 3)), "years")

    # def calculate_age(self):
    #     date = self.birthday_book[1][0]
    #     birthday = datetime.strptime(date, "%Y-%m-%d")

    #     self.today = datetime.today()  # this is a datetime object

    #     # try:
    #     #     d2 = datetime.strptime(date_of_birth, "%Y-%m-%d") #converts a string into a datetime object
    #     # except ValueError:
    #     #     return "Please enter a valid format"

    #     # age = math.floor((datetime.today() - d2).days / 365)
    #     return birthday

    def update_date(self, name, date):
        # Parameters:
        #   name: string representing a name
        #   date: string representing a date
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the new date to the corresponding name
        pass  # No code here yet

    def update_name(self, old_name, new_name):
        # Parameters:
        #   old_name: string representing the old name
        #   new_name: string representing the new name
        # Returns:
        #   Nothing
        # Side-effects
        #   Update new name in entry
        pass  # No code here yet

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
