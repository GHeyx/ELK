#This is a Person class that will be used to create a person object for a person's card in a family tree application
class Person:
    def __init__(self, name, age, dob, pob, occupation):
        self.name = name
        self.age = age
        self.dob = dob
        self.pob = pob
        self.occupation = occupation
        self.achievements = []
        self.hobbies = []


    def __str__(self):
        return "Person: {} is"