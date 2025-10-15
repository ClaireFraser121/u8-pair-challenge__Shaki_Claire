# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user [1]
So I don't forget the details
I want to keep a record of friends' names and birthdates

As a user [2]
So I can make edits when I've got dates wrong
I want to be able to update a record by passing in a name and new date

As a user [3]
So I can make edits when people change their name
I want to be able to update a record by passing in an old and a new name

As a user [4]
So I can remember to send birthday cards at the right time
I want to be able to list friends whose birthdays are coming up soon and to whom I need to send a card

As a user [5]
So I can buy age-appropriate birthday cards
I want to calculate the upcoming ages for friends with birthdays

As a user [6]
So I can keep track of cards sent and to be sent
I want to be able to mark a birthday card for a year as "done"

"""
You may want to make use of the `datetime and dateutil` libraries here. It's good practice - dates and/or times are necessary parts of many applications, as are the calculations between pairs of them.

"""

1. keep record of names and birthdays
2. update dates by passing name and date
3. update name by passing old and new name
4. list upcoming birthdays with correct names
5. for each birthday calculate age 
6. mark cards sent as done


## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class BirthdayReminder:
    # User-facing properties:
    #   name: string

    def __init__(self):
        # Parameters:
        #   none
        # Side effects:
        #   create dict 
        #   {name : {birthday: birthdate, age: #calculate_age, card_status: "not sent"}}
        pass # No code here yet

    def add(self, name, date):
        # Parameters:
        #   name: string representing a name 
        #   date: string representing a date
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves name and date to the dict
        pass # No code here yet

    def update_date(self, name, date):
        # Parameters:
        #   name: string representing a name 
        #   date: string representing a date
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the new date to the corresponding name
        pass # No code here yet

    def update_name(self, old_name, new_name):
        # Parameters:
        #   old_name: string representing the old name 
        #   new_name: string representing the new name
        # Returns:
        #   Nothing
        # Side-effects
        #   Update new name in entry
        pass # No code here yet

    def upcoming_birthdays(self):
        # Parameters:
        #   self
        # Returns:
        #   upcoming birthdays, names, age, and card status (done/not done)
        # Side-effects
        #   none
        pass # No code here yet

    def calculate_age(self):
        # Parameters:
        #   self.birthdate
        # Returns:
        #   calculated age
        # Side-effects
        #   store age in entry
        pass # No code here yet

    def send_card(self, name):
        # Parameters:
        #   name: a string representing a name 
        # Returns:
        #   string: "You have sent a card to {name}"
        # Side-effects
        #   add done to to the entry
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

1. keep record of names and birthdays
2. update dates by passing name and date
3. update name by passing old and new name
4. list upcoming birthdays with correct names and card status
5. for each birthday calculate age 
6. mark cards sent as done

``` python
# EXAMPLE

"""
(1A)
Given a name and birthday check if it they 
are stored properly in the instance.
{name : {birthday: birthdate, age: #calculate_age, card_status: "not sent"}}
"""
birthday_reminder = BirthdayReminder()
birthday_reminder.add("Sandra", "30/06/2018")
birthday_reminder.birthday_book  # =>  {"Sandra" : {birthday: "30/06/2018", age: 7, card_status: "not sent"}}

"""
(1B)
Given multiple names and birthdays 
All are stored correctly in the dict
"""
birthday_reminder = BirthdayReminder()
birthday_reminder.add("Sandra", "30/06/2018")
birthday_reminder.add("Maria", "15/10/2000")
birthday_reminder.add("Mark", "04/11/1998")
birthday_reminder.birthday_book  # => {"Sandra" : {birthday: "30/06/2018", age: 7, card_status: "not sent"}, "Maria" : {birthday: "15/10/2000", age: 25, card_status: "not sent"}, "Mark : {birthday: "04/11/1998", age: 26, card_status: "not sent"}}


"""
(1C)
Given an empty name 
It throws an exception
"""
birthday_reminder = BirthdayReminder()
birthday_reminder.add("", "30/06/2018") # => "Please enter valid name!"

"""
(1D)
Given an empty  date 
It throws an exception
"""
birthday_reminder = BirthdayReminder()
birthday_reminder.add("Sandra", "") # => "Please enter valid date!"

"""
(2A)
Given an existing name and valid date
#update_date successful updated the date 
"""
birthday_reminder = BirthdayReminder()
birthday_reminder.add("Sandra", "30/06/2018")
birthday_reminder.update_date("Sandra", "31/06/2018")
birthday_reminder.birthday_book  # => {"Sandra" : {birthday: "30/06/2018", age: 7, card_status: "not sent"}}


"""
(2B)
Having two contacts in the birthday book 
and editing one of the dates
Given an existing name and valid date
#update_date successful updated the date 
"""
birthday_reminder = BirthdayReminder()
birthday_reminder.add("Sandra", "30/06/2018")
birthday_reminder.add("Maria", "15/10/2000")
birthday_reminder.update_date("Sandra", "31/06/2018")
birthday_reminder.birthday_book  # => {"Sandra" : {birthday: "31/06/2018", age: 7, card_status: "not sent"}, "Maria" : {birthday: "15/10/2000", age: 25, card_status: "not sent"}}


"""
(3A)
Having two contacts in the birthday book 
and editing one of the names
Given an old name and new name
#update_name successful updated the name 
"""
birthday_reminder = BirthdayReminder()
birthday_reminder.add("Sadra", "30/06/2018")
birthday_reminder.add("Maria", "15/10/2000")
birthday_reminder.update_name("Sadra", "Sandra")
birthday_reminder.birthday_book  # => {"Sandra" : {birthday: "30/06/2018", age: 7, card_status: "not sent"}, "Maria" : {birthday: "15/10/2000", age: 25, card_status: "not sent"}}



"""
(4A)
Given the current date 
#upcoming_birthdays returns upcoming birthdays for the next month 
"""

birthday_reminder = BirthdayReminder()
birthday_reminder.add("Sandra", "30/06/2018")
birthday_reminder.add("Maria", "29/10/2000")
birthday_reminder.upcoming_birthdays() # => {"Maria" : {birthday: "29/10/2000", age: 25, card_status: "not sent"}}


"""
(4B)
Given the current date 
#upcoming_birthdays returns upcoming for multiple birthdays for the next month 
"""

birthday_reminder = BirthdayReminder()
birthday_reminder.add("Sandra", "30/06/2018")
birthday_reminder.add("Maria", "29/10/2000")
birthday_reminder.add("Mark", "04/11/1998")
birthday_reminder.upcoming_birthdays() # => {"Maria" : {birthday: "29/10/2000", age: 25, card_status: "not sent"}, "Mark : {birthday: "04/11/1998", age: 26, card_status: "not sent"}}

"""
(5A)
Given a birthdate
#calculate_age returns age as an integer
"""
birthday_reminder = BirthdayReminder()
birthday_reminder.add("Sandra", "30/06/2018")
birthday_reminder.calculate_age() # 7
#birthday_reminder.birthday_book # => {{"Sandra" : {birthday: "30/06/2018", age: 7, card_status: "not sent"}}


"""
(5A)
Given name and birthday 
#send_card marks card_status as "sent"
"""
birthday_reminder = BirthdayReminder()
birthday_reminder.add("Sandra", "30/06/2018")
birthday_reminder.send_card() 
birthday_reminder.birthday_book # => {{"Sandra" : {birthday: "30/06/2018", age: 7, card_status: "sent"}}
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
