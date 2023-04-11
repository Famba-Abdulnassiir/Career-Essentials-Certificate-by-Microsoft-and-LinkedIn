class puppy ():
    def __init__(self,name, favourite_toy) -> None:
        self.name = name
        self.favourite_toy = favourite_toy

    def play(self):
        print(self.name + "is playing with the " + self.favourite_toy)

marble = puppy("Marble", "Teddy bear")
marble.play()

onyx = puppy("onyx", "lizard")
onyx.play() 


# A class is a blueprint or template that defines the structure and behavior of objects. 
# It encapsulates data (in the form of attributes or properties) and methods (functions or behaviors) 
# that operate on that data. An object is an instance of a class, created from the class blueprint, 
# which can be used to interact with the data and methods defined in the class.

#Another Example is here
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def say_hello(self):
        print(f"Hello, my name is {self.name}. I'm {self.age} years old, and I'm {self.gender}.")

person1 = Person("Alice", 30, "female")
person2 = Person("Bob", 25, "male")

print(person1.name) # Output: Alice
print(person2.age) # Output: 25

person1.say_hello() # Output: Hello, my name is Alice. I'm 30 years old, and I'm female.
person2.say_hello() # Output: Hello, my name is Bob. I'm 25 years old, and I'm male.
