# Given the below class:
class Cat:
    species = "mammal"

    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat("Tom", 8)
cat2 = Cat("Mustafá", 11)
cat3 = Cat("Molly", 9)


# 2 Create a function that finds the oldest cat
# def find_oldest_cat():
#     cats = [cat1, cat2, cat3]
#     oldest_cat = max(cats, key=lambda cat: cat.age)
#     return oldest_cat


oldest_cat = max(cat1.age, cat2.age, cat3.age)

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2

# print(f"The oldest cat is {find_oldest_cat().age} years old.")
print(f"The oldest cat is {oldest_cat} years old.")
