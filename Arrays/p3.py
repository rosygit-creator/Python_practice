class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # def __str__(self):
    #     return self.name , self.age

# p1 = Person("John", 36)

class Subclass(Person):
    def __init__(self, name, age, year):
        super().__init__(name,age)
        self.year=year

    def printval(self):
        print(self.age, self.name, self.year)

s1=Subclass("rosy",1, 2025)
s1.printval()


# class Publication:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# class Book(Publication):
#     def __init__(self, name, age, year):
#         # Correct: self is implicit in super().__init__()
#         super().__init__(name, age)
#         self.year = year
#
# # Correct usage
# my_book = Book("The Great Gatsby", 10.99, "F. Scott Fitzgerald")
# print(my_book.year)