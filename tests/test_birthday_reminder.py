import pytest
from lib.BirthdayReminder import BirthdayReminder

"""
(1)
init class 
self.birthday book dict exists
"""
def test_init_dict():
    birthday_reminder = BirthdayReminder()
    assert birthday_reminder.birthday_book == {}

"""
(1A)
Given a name and birthday check if it they
are stored properly in the instance.
{name : {birthday: birthdate, "age": #calculate_age, "card_status": "not sent"}}
"""
def test_name_and_birthday_are_stored():
    birthday_reminder = BirthdayReminder()
    birthday_reminder.add("Sandra", "30-06-2018")
    # print(birthday_reminder.calculate_age())
    assert birthday_reminder.birthday_book == {
        "Sandra": {"birthday": "30-06-2018", "age": 7, "card_status": "not sent"}
    }

"""
(1B)
Given multiple names and birthdays
All are stored correctly in the dict
"""
def test_multiple_names_and_birthdays_store_correctly():
    birthday_reminder = BirthdayReminder()
    birthday_reminder.add("Sandra", "30-06-2018")
    birthday_reminder.add("Maria", "15-10-2000")
    birthday_reminder.add("Mark", "04-11-1998")
    assert birthday_reminder.birthday_book == {
        "Sandra": {"birthday": "30-06-2018", "age": 7, "card_status": "not sent"},
        "Maria": {"birthday": "15-10-2000", "age": 25, "card_status": "not sent"},
        "Mark": {"birthday": "04-11-1998", "age": 26, "card_status": "not sent"},
    }


"""
(1C)
Given an empty name
It throws an exception
"""
def test_empty_name_raises_error():
    birthday_reminder = BirthdayReminder()
    with pytest.raises(Exception) as e:
        birthday_reminder.add("", "30-06-2018")
    error_message = str(e.value)
    assert error_message == "Please enter valid name!"

"""
(1D)
Given an empty  date
It throws an exception
"""
def test_empty_date_raises_error():
    birthday_reminder = BirthdayReminder()
    with pytest.raises(Exception) as e:
        birthday_reminder.add("Sandra", "")
    error_message = str(e.value)
    assert error_message == "Please enter valid date!"

"""
(2A)
Test if edits update date
Given an existing name and valid date
#update_date successful updated the date
"""
def test_if_edits_update_date():
    birthday_reminder = BirthdayReminder()
    birthday_reminder.add("Sandra", "30-06-2018")
    birthday_reminder.update_date("Sandra", "31-06-2018")
    assert birthday_reminder.birthday_book  == {"Sandra" : {"birthday": "31-06-2018", "age": 7, "card_status": "not sent"}}

"""
(2Aa)
Test if edits update date
Given an existing name and valid date
#update_date successful updated the date and age
"""
def test_if_edits_update_date():
    birthday_reminder = BirthdayReminder()
    birthday_reminder.add("Sandra", "30-06-2018")
    birthday_reminder.update_date("Sandra", "30-06-2019")
    assert birthday_reminder.birthday_book  == {"Sandra" : {"birthday": "30-06-2019", "age": 7, "card_status": "not sent"}}


"""
(2B)
Having two contacts in the birthday book
and editing one of the dates
Given an existing name and valid date
#update_date successful updated the date
"""
def test_if_date_edits_work_if_multiple_names_in_dict():
    birthday_reminder = BirthdayReminder()
    birthday_reminder.add("Sandra", "30-06-2018")
    birthday_reminder.add("Maria", "15-10-2000")
    birthday_reminder.update_date("Sandra", "31-06-2018")
    assert birthday_reminder.birthday_book  == {"Sandra" : {"birthday": "31-06-2018", "age": 7, "card_status": "not sent"}, "Maria" : {"birthday": "15-10-2000", "age": 25, "card_status": "not sent"}}


"""
(3A)
Having two contacts in the birthday book
and editing one of the names
Given an old name and new name
#update_name successful updated the name
"""
def test_if_name_edit_works_if_multiple_names_in_dict():
    birthday_reminder = BirthdayReminder()
    birthday_reminder.add("Sadra", "30-06-2018")
    birthday_reminder.add("Maria", "15-10-2000")
    birthday_reminder.update_name("Sadra", "Sandra")
    assert birthday_reminder.birthday_book  == {"Sandra" : {"birthday": "30-06-2018", "age": 7, "card_status": "not sent"}, "Maria" : {"birthday": "15-10-2000", "age": 25, "card_status": "not sent"}}


"""
(4A)
Given the today's date
#upcoming_birthdays returns upcoming birthdays for the next month
"""
def test_if_today_return_upcoming_birthdays():
    birthday_reminder = BirthdayReminder()
    birthday_reminder.add("Sandra", "30-06-2018")
    birthday_reminder.add("Maria", "29-10-2000")
    assert birthday_reminder.upcoming_birthdays() == "Maria"


"""
(4B)
Given the current date
#upcoming_birthdays returns upcoming for multiple birthdays for the next month
"""
def test_if_upcoming_birthdays_returns_for_multiple_people():
    birthday_reminder = BirthdayReminder()
    birthday_reminder.add("Sandra", "30-06-2018")
    birthday_reminder.add("Maria", "29-10-2000")
    birthday_reminder.add("Mark", "04-11-1998")
    assert birthday_reminder.upcoming_birthdays() == "Maria, Mark"

"""
(6A)
Given name
#send_card marks card_status as "sent"
"""
def test_if_cards_marked_as_sent():
    birthday_reminder = BirthdayReminder()
    birthday_reminder.add("Sandra", "30-06-2018")
    birthday_reminder.send_card("Sandra")
    assert birthday_reminder.birthday_book == {"Sandra" : {"birthday": "30-06-2018", "age": 7, "card_status": "sent"}}

"""
(6B)
Given name for a card that has already been sent
#send_card raises exception
"""
def test_if_cards_marked_as_sent():
    birthday_reminder = BirthdayReminder()
    birthday_reminder.add("Sandra", "30-06-2018")
    birthday_reminder.send_card("Sandra")
    with pytest.raises(Exception) as e:
        birthday_reminder.send_card("Sandra")
    assert str(e.value) == "Card already sent!"

"""
(6C)
Given a name
check card_status is "not sent"
"""
def test_card_not_sent():
    birthday_reminder = BirthdayReminder()
    birthday_reminder.add("Sandra", "30-06-2018")
    birthday_reminder.add("Alex", "01-01-2018")
    birthday_reminder.send_card("Sandra")
    assert birthday_reminder.birthday_book["Alex"]["card_status"] == "not sent"
