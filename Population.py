"""
Define class Human which has the following : gender hair eyes AGE
For every baby a Human gets Population must be += 1
Only women can have babies
Human grows from baby > child > adolescent > adult
The attributes gender hair eyes are randomly given to Human
Give population a starting number  and make that amount of humans
"""
import random

total_population = 4
genderoptions = ['M', 'F']
hairoptions = ["blond", "brown", "black", "ginger"]
eyesoptions = ["blue", "green", "brown"]
ageoptions = ['baby', 'child', 'adolescent', 'adult']

class Human:

    kind = 'homo_sapiens'

    def __init__(self, gender, hair, eyes, age):
        self.gender = random.choice(genderoptions)
        self.hair = random.choice(hairoptions)
        self.eyes = random.choice(eyesoptions)
        self.age = age

   #def __set_characteristics(self, gender, hair, eyes):
        # """
        # the __ before function name makes it private - that means it can only be used within this class
        # """
    #    self.gender =
    #    self.hair =
    #    self.eyes =

    def make_baby(self, gender, hair, eyes, age):
        if Human.gender == "F" and age == "adult":
            total_population +=1
            print("There are now %i people") %total_population
            return Human(self, gender, hair, eyes, "baby")
        else:
            pass

Adam = Human('M', 'ginger', 'green')
Eva = Human('F', 'blond', 'brown')
Joseph = Human('M', 'brown', 'blue')
Mary = Human('F', 'black', 'brown')

print("Do you want to make babies?")
answer = str(raw_input("yes/no "))

if 'y' in answer:
    pass # make babies

