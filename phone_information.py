# Create your Contact class here

# Your Contact class should have THREE attributes: first_name, last_name, and phone_number
# These attributes must get their values from the constructor arguments (i.e. in your main.py in the code you're instructed not to modify, a first name, last name, and phone number are all passed IN THAT ORDER to each of the calls to the Contact() constructor)
# You should override the dunder methods for __eq__ (equality), __lt__ (less than), and __gt__ (greater than) so that your search will work

class Contact():
  def __init__(self, first_name, last_name, phone_number):
    self.first_name = first_name 
    self.last_name = last_name 
    self.phone_number = phone_number  
  
  def __eq__(self, other):
    if self.first_name == other.first_name and self.last_name == other.last_name:
      return True
    return False 
  
  def __gt__(self, other):
    if self.first_name > other.first_name:
      return True 
    return False 
  
  def __lt__(self, other):
    if self.first_name < other.first_name:
      return True 
    return False
  
  def __str__(self):
    ret = ''
    ret += f'\nFirst: {self.first_name}\nLast: {self.last_name}\nNumber: {self.phone_number}\n\n'
    return ret

def get_new_contact():
  user_raw = input('Enter the new contact first name, last name, and phone number in a comma separated list: ')
  user_data = list(map(lambda x: x.strip(), user_raw.split(',')))
  first, last, num = user_data
  return (first, last, num)
    
def add_contact(sort_func, items):
  first, last, num = get_new_contact()
  new_contact = Contact(first, last, num)
  items.append(new_contact)
  sort_func(items)
  print(f'\n{first} contact added!\n')

def get_contact():
  user_raw = input('\nEnter the contact first and last name to search in a comma separated list:\n ')
  user_data = list(map(lambda x: x.strip(), user_raw.split(',')))
  first, last = user_data
  return (first, last)

def find_contact(search_func, items):
  first, last = get_contact()
  num = 123 
  test_contact = Contact(first, last, num)
  # print(test_contact)
  find = search_func(items, 0, len(items)-1, test_contact)
  #print('find index', find)
  if find != -1:
    print(f'\nIndex: {find}\n {items[find]}\n')
  else:
    print(f'\nContact not found!\n')