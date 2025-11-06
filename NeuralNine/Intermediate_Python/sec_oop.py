class Person:

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    
    def __str__(self):
        return "Name: {}, age: {}, height: {}".format(self.name, self.age, self.height)
    
class Worker(Person):

    def __init__(self, name, age, height, salary):
        super(Worker,self).__init__(name, age, height)
        self.salary = salary

    def calc_yearly_salary(self):
        return self.salary * 12

    def __str__(self):
        text = super(Worker,self).__str__()
        text += ", Yearly salary: {}".format(self.salary)
        return text

worker1 = Worker("Mike",24,178,25000) 

# Since this is not invoking calc_yearly_salary() therefore it will only tell us what we added. To check yearly, check function below this.
print(worker1) 

print(worker1.calc_yearly_salary())