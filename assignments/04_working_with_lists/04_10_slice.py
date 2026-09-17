animals = ["foxes", "cats", "squirrels", "bunnies", "dogs"]
number = 1

for animal in animals:
    print(f"{animal.title()} are my number {number} favorite animal!")
    number += 1

print("\nAll of these animals have a tail.")

print("\nThe first three animals in the list are:")
for animal in animals[:3]:
    print(animal.title())

print("\nThree animals from the middle of the list are:")
for animal in animals[1:4]:
    print(animal.title())

print("\nThe last three animals in the list are:")
for animal in animals[-3:]:
    print(animal.title())