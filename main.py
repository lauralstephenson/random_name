names = ["Angela", "Ben", "Jenny", "Michael", "Chloe"]
names = names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆
import random

result = random.choice(names)
print(f"{result} is going to buy the meal today!")

#OR
#get the total number of list items
#num_items = len(names)
#Generate random numbers between 0 and the last index
#random_choice = random.randint(0, num_items - 1)
#Choose and print a random name from the list
#print(names[random_choice])Fiz