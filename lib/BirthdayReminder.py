class BirthdayReminder:
    # User-facing properties:
    #   name: string

    def __init__(self):
        self.birthday_book = {}

    def add(self, name, date):
        # Parameters:
        #   name: string representing a name
        #   date: string representing a date
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves name and date to the dict
        pass  # No code here yet

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

    def calculate_age(self):
        # Parameters:
        #   self.birthdate
        # Returns:
        #   calculated age
        # Side-effects
        #   store age in entry
        pass  # No code here yet

    def send_card(self, name):
        # Parameters:
        #   name: a string representing a name
        # Returns:
        #   string: "You have sent a card to {name}"
        # Side-effects
        #   add done to to the entry
        pass  # No code here yet
