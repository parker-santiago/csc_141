pizza = ["pepperoni", "the works", "cheese"]
friend_pizza = pizza[:]

pizza.append("bacon & ham")
friend_pizza.append("vegetarian")

for pizza in pizza:
    print(f"I like {pizza} pizza!")
print("\nI think pizza is alright\n")

for pizza in friend_pizza:
    print(f"My friend likes {pizza} pizza!")
print("\nMy friend loves pizza")