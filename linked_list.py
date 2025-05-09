from node import Node

class Phonebook():
  def __init__(self):
    self.head = None
  
  def add_contact(self, contact):
    new_contact = Node(contact)
    if self.head == None:
      self.head = new_contact 
    else:
      self.head.next = new_contact 
  