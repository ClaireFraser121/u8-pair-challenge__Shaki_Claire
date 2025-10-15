from lib.BirthdayReminder import BirthdayReminder

"""
(1)
init class 
self.birthday book dict exists
"""


def test_init_dict():
    birthday_reminder = BirthdayReminder()
    assert birthday_reminder.birthday_book == {}


# """
# (1A)
# Given a name and birthday check if it they
# are stored properly in the instance.
# {name : {birthday: birthdate, "age": #calculate_age, "card_status": "not sent"}}
# """


# def test_name_and_birthday_are_stored():
#     birthday_reminder = BirthdayReminder()
#     birthday_reminder.add("Sandra", "30/06/2018")
#     assert birthday_reminder.birthday_book == {
#         "Sandra": {"birthday": "30/06/2018", "age": 7, "card_status": "not sent"}
#     }


# """
# (1B)
# Given multiple names and birthdays
# All are stored correctly in the dict
# """
# birthday_reminder = BirthdayReminder()
# birthday_reminder.add("Sandra", "30/06/2018")
# birthday_reminder.add("Maria", "15/10/2000")
# birthday_reminder.add("Mark", "04/11/1998")
# birthday_reminder.birthday_book  # => {"Sandra" : {"birthday": "30/06/2018", "age": 7, ""card_status"": "not sent"}, "Maria" : {"birthday": "15/10/2000", "age": 25, ""card_status"": "not sent"}, "Mark : {"birthday": "04/11/1998", "age": 26, "card_status": "not sent"}}


# """
# (1C)
# Given an empty name
# It throws an exception
# """
# birthday_reminder = BirthdayReminder()
# birthday_reminder.add("", "30/06/2018") # => "Please enter valid name!"

# """
# (1D)
# Given an empty  date
# It throws an exception
# """
# birthday_reminder = BirthdayReminder()
# birthday_reminder.add("Sandra", "") # => "Please enter valid date!"

# """
# (2A)
# Given an existing name and valid date
# #update_date successful updated the date
# """
# birthday_reminder = BirthdayReminder()
# birthday_reminder.add("Sandra", "30/06/2018")
# birthday_reminder.update_date("Sandra", "31/06/2018")
# birthday_reminder.birthday_book  # => {"Sandra" : {"birthday": "30/06/2018", "age": 7, "card_status": "not sent"}}


# """
# (2B)
# Having two contacts in the birthday book
# and editing one of the dates
# Given an existing name and valid date
# #update_date successful updated the date
# """
# birthday_reminder = BirthdayReminder()
# birthday_reminder.add("Sandra", "30/06/2018")
# birthday_reminder.add("Maria", "15/10/2000")
# birthday_reminder.update_date("Sandra", "31/06/2018")
# birthday_reminder.birthday_book  # => {"Sandra" : {"birthday": "31/06/2018", "age": 7, "card_status": "not sent"}, "Maria" : {"birthday": "15/10/2000", "age": 25, "card_status": "not sent"}}


# """
# (3A)
# Having two contacts in the birthday book
# and editing one of the names
# Given an old name and new name
# #update_name successful updated the name
# """
# birthday_reminder = BirthdayReminder()
# birthday_reminder.add("Sadra", "30/06/2018")
# birthday_reminder.add("Maria", "15/10/2000")
# birthday_reminder.update_name("Sadra", "Sandra")
# birthday_reminder.birthday_book  # => {"Sandra" : {"birthday": "30/06/2018", "age": 7, "card_status": "not sent"}, "Maria" : {"birthday": "15/10/2000", "age": 25, "card_status": "not sent"}}


# """
# (4A)
# Given the current date
# #upcoming_birthdays returns upcoming birthdays for the next month
# """

# birthday_reminder = BirthdayReminder()
# birthday_reminder.add("Sandra", "30/06/2018")
# birthday_reminder.add("Maria", "29/10/2000")
# birthday_reminder.upcoming_birthdays() # => {"Maria" : {"birthday": "29/10/2000", "age": 25, "card_status": "not sent"}}


# """
# (4B)
# Given the current date
# #upcoming_birthdays returns upcoming for multiple birthdays for the next month
# """

# birthday_reminder = BirthdayReminder()
# birthday_reminder.add("Sandra", "30/06/2018")
# birthday_reminder.add("Maria", "29/10/2000")
# birthday_reminder.add("Mark", "04/11/1998")
# birthday_reminder.upcoming_birthdays() # => {"Maria" : {"birthday": "29/10/2000", "age": 25, "card_status": "not sent"}, "Mark : {"birthday": "04/11/1998", "age": 26, "card_status": "not sent"}}

# """
# (5A)
# Given a birthdate
# #calculate_age returns age as an integer
# """
# birthday_reminder = BirthdayReminder()
# birthday_reminder.add("Sandra", "30/06/2018")
# birthday_reminder.calculate_age() # 7
# #birthday_reminder.birthday_book # => {{"Sandra" : {"birthday": "30/06/2018", "age": 7, "card_status": "not sent"}}


# """
# (6A)
# Given name and birthday
# #send_card marks card_status as "sent"
# """
# birthday_reminder = BirthdayReminder()
# birthday_reminder.add("Sandra", "30/06/2018")
# birthday_reminder.send_card()
# birthday_reminder.birthday_book # => {{"Sandra" : {"birthday": "30/06/2018", ""age"": 7, "card_status": "sent"}}
