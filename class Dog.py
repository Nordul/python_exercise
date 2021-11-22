class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def sit(self):
        print(f'{self.name} is now sitting')

    def roll_over(self):
        print(f'{self.name} rolled over!')


my_dog = Dog('willie',6)
your_dog = Dog('Lucy',3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog's is {my_dog.age} years old.")
print(f'{my_dog.name},sit!')
my_dog.sit()


print(f"Your dog's name is {your_dog.name}.")
print(f"Your dog's is {your_dog.age} years old.")
print(f'{your_dog.name}, roll around!')
your_dog.roll_over()