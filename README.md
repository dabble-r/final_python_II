# final_python_II

In this assignment, you will create an address book based off of preliminary code. This address book will sort a list of contacts and allow the user to search for a specific contact. You will have to create your own Contact class, build your own sorting algorithm and searching algorithm, and apply them in a main program.

Preliminary code to set this up has already been written for you to build the address book and will be provided. Do NOT modify ANY pre-written code. Modifying any prewritten code WILL RESULT IN A 0. Trying to overwrite any prewritten code WILL RESULT IN A 0. When you open it you should look at the code and files present before you dive into coding.

When you start the quiz, you will be given the starter files AND specific instructions to get started.
You may NOT begin coding until you begin the quiz.

Below is some GENERAL INFORMATION about what you will be required to do so that you can gather your notes and textbook materials and prepare accordingly. Remember: You CAN USE YOUR TEXTBOOKS! You CAN USE NOTES! I advise you work out the logical steps for this project in a notebook so that you are prepared to code.

You may not write any code in advance. If you write code in advance you will receive a 0.

Create a Contact class in the provided file phone_information.py with the required attributes, import to main.py as needed
Create your own sorting algorithm in the provided file algorithms.py, import to main.py as needed (you may NOT use any built in sort functions!)
the best sorting algorithm is an efficient algorithm
Create your own binary searching algorithm in algorithms.py, import to main.py as needed
Apply your sorting algorithm in main.py to the contact_list variable ALREADY PROVIDED FOR YOU (DO NOT MODIFY OR YOU WILL GET A 0!!!) so that your contact_list will be SORTED ALPHABETICALLY BY FIRST NAME
In main.py, create a menu that prompts the user to choose to do the following:
Show all contacts
Add a new contact
Search for a specific contact
Quit the program
If a user chooses number 1 "Show all contacts" then the program should print out each contact in the address book first name last name phone number) on a new line
If a user chooses number 2 "Add a new contact" then the program should prompt the user for the contact's first name then prompt for the contact's last name then prompt for the contact's phone number. The contact should then be added to the list. The list should then be SORTED ALPHABETICALLY BY FIRST NAME using YOUR OWN SORTING ALGORITHM
If a user chooses number 3 "Search for a specific contact" then the program should prompt the user for the contact's first and last name. Then the program should apply your searching algorithm.
if the contact is found, print out the contact's first name, last name, and phone number
if the contact is not found, you must state that the contact is not found.
If a user chooses number 4 "Quit the program" the program should end. The program should NOT terminate UNLESS this option is selected.
If a user chooses any other number, the program should inform the user that is not an appropriate choice and re-prompt the user for an appropriate choice.
You will have 6 hours to complete this or until the assignment closes, whichever comes first. This assignment uses Honorlock. Short breaks are allowed.

Helpful Hints & Reminders
the program should not terminate after a user makes any selection (except the "Quit the program" selection). To ensure this happens, a loop should be used.
before you can perform a binary search, your list must be sorted. Any time you add a new contact, that means you need to resort your list after the addition.
do not forget that you WILL need to overwrite dunder methods in the Contact class before you do anything. Pay close attention to Figure 23-9 in your Programming with Python (McMullen) text, accessed via Course Materials
Review chapters 23 and 24 in your Programming with Python (McMullen) text, accessed via Course Materials
