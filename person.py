from tkinter import *
# This is a Person class that will be used to create a person object for a person's card in a family tree application
# The person class will be required to have the following attributes: first name, last name, gender, date of birth, place of birth 

# The following atttributes will be optional:
class Person:
    def __init__(self, firstName, lastName, gender, dob, pob, occupation):
        self.firstName = firstName
        self.lastName = lastName
        self.gender = gender
        self.dob = dob
        self.pob = pob
        self.occupation = occupation
        self.achievements = []
        self.hobbies = []


    def __str__(self):
        return "Person: {} is"

root = Tk()
#Landing Page GUI
offlineButton = Button(root, text="Offline Mode")
onlineButton = Button(root, text="Go Online")
# logo = PhotoImage(file="family tree\Application Images\temp logo.png")

offlineButton.pack()
onlineButton.pack()
# logo.pack()
root.mainloop()
