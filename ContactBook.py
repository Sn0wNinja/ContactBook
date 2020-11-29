from pyfiglet import figlet_format
from termcolor import colored

contact_book = {}
on = True

def add_contact():
    global contact_book
    name = input("Please add name of the contact: ")
    number = input(f"Please add phone number of {name}: ")
    contact_book[name] = number
    print("")
    print(contact_book)

def remove_contact():
    global contact_book
    name = input("Please enter the name of the contact you want to remove: ")
    if name in contact_book:
        del contact_book[name]
        print("")
        print(f"Contact info of {name} was deleted")
    else:
    	print("")
    	print("The name that you provided doesn't match any of the contacts")

def show_phone_num():
    global contact_book
    name = input("Please enter the name of the contact you want to show: ")
    if name in contact_book:
    	print("")
    	print(f"The phone number you are asking for: {contact_book.get(name)}")
    else:
    	print("")
    	print("The name that you provided doesn't match any of the contacts")

def change_phone_num():
    global contact_book
    name = input("Please enter who's contact info you would like to change: ")
    new_number = input("Please enter his new contact: ")
    if name in contact_book:
        contact_book[name] = new_number
        print("")
        print(f"Contact info of {name} changed to {contact_book[name]}")
    else:
    	print("")
    	print("The name that you provided doesn't match any of the contacts")

def show_contact_book():
	global contact_book
	print("")
	print(contact_book)

header = figlet_format("CONTACT BOOK")
header = colored(header, color = "yellow")
print("")
print(header)

while on:

	print("")
	print("What would you like to do? \nPlease enter a number: \n1 Add new contact \n2 Remove a contact \n3 Show contact of a given name \n4 Change contact information \n5 Show entire contact book \n6 End the App")
	intro_num = input()

	if intro_num == "1":
		add_contact()

	elif intro_num == "2":
		remove_contact()

	elif intro_num == "3":
		show_phone_num()

	elif intro_num == "4":
		change_phone_num()

	elif intro_num == "5":
		show_contact_book()

	elif intro_num == "6":
		print("")
		print("Thank you for using our App, have a great rest of the day!")
		on = False














