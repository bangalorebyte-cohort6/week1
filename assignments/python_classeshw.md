## Python Classes

Submit the following by Thursday, January 26th, 2017 at 6:10pm. 

### Part 1 

In your `README.txt` answer the questions below. Recall that `scope` refers to  which parts of your code can use a given object. For example, global variables can be used by the rest of the code since it is global.

Here is an example of a simple class which stores information about a person:
``` python
import datetime # we will use this for date objects

class Person:

    def __init__(self, name, surname, birthdate, address, telephone, email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate

        self.address = address
        self.telephone = telephone
        self.email = email

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year

        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1

        return(age)
        
person = Person(
    "Jane",
    "Doe",
    datetime.date(1992, 3, 12), # year, month, day
    "No. 12 Short Street, Greenville",
    "555 456 0987",
    "jane.doe@example.com"
)

print(person.name)
print(person.email)
print(person.age())
```
Explain what the following variables refer to, and their scope:

1. `Person`
2. `person`
3. `surname`
4. `self`
5. `age` (the function name)
6. `age` (the variable used inside the function)
7. `self.email`
8. `person.email`


### Part 2

Using the [Luhn Algorithm](http://en.wikipedia.org/wiki/Luhn_algorithm), also known as "modulus 10", we will be determining the validity of a given credit card number.

For now, you are just editing the included python file. You will find the skeleton of the `CreditCard` class inside. We want our class to have its three main properties set on [instantiation](http://en.wikipedia.org/wiki/Instance_(computer_science)) - card_number, card_type, and valid. Look at the code, you'll see this already there.

If the card number given passes the Luhn algorithm, valid should be true and cardType should be set to 'VISA', 'AMEX', etc. If it does not pass, valid should be false and cardType should be set to "INVALID"

This way, we can do this:
```python
    myCard = CreditCard('347650202246884')

    myCard.valid ## true
    myCard.card_type ## 'AMEX'
    myCard.card_number ## '347650202246884'
```

There are three instance methods. You may perform these methods in the order you see fit.

`determine_card_type` should check whether or not the credit card has valid starting numbers and return the card type.

Visa must start with 4  
Mastercard must start with 51, 52, 53, 54 or 55  
AMEX must start with 34 or 37  
Discover must start with 6011  

`check_length` should check whether or not a credit card number is a valid length.

Visa, MC and Discover have 16 digits  
AMEX has 15  

`validate` should run the Luhn Algorithm and return true or false.

The algorithm should works as follows: 

From the right most digit, double the value of every second digit. For example:

`4 4 8 5 0 4 0 9 9 3 2 8 7 6 1 6`

becomes

`8 4 16 5 0 4 0 9 18 3 4 8 14 6 2 6`

Now, sum all the individual digits together. That is to say, split any numbers with two digits into their individual digits and add them. Like so:

`8 + 4 + 1 + 6 + 5 + 0 + 4 + 0 + 9 + 1 + 8 + 3 + 4 + 8 + 1 + 4 + 6 + 2 + 6`

Now take the sum of those numbers and modulo 10.

80 % 10

If the result is 0, the credit card number is valid.

Keep your code super clean and [DRY](http://en.wikipedia.org/wiki/Don't_repeat_yourself). If you are repeating yourself, stop and think about how to better approach the problem. Keep your code encapsulated - imagine your CreditCard class is an interface other code will need to read. You want it as separate and unentangled as possible. Your class should not be dependent on any code outside of it - except, of course, code to instantiate it.



