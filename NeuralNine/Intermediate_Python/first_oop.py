class Person:

    amount = 0

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        Person.amount += 1

    def __del__(self):

         Person.amount -= 1

    # Not Used very often
    #def __del__(self):
    #    print("Object got deleted")

    def __str__(self):
        return "Name: {}, Age: {}, Height: {}".format(self.name,self.age,self.height)

person1 = Person("Mike", 25, 180)

person2 = Person('sara',27,150)
#print(person1.name)

#print(person1.age)
#print(person1.height)

# Changing the name in object called person1
#person1.name = "Henry"

# Deleteing an Object
# del person1

#del person2
print(Person.amount)