active = True
responses = {}
while active:
    name = input("What is your name? ")
    location = input("Where would you like to go on your dream vacation? ")
    responses[name] = location
    continue_vacation = input("Would you like to let another person respond? (yes/no): ")
    if continue_vacation.lower() != "yes":
        active = False

print("\nDream vacation responses:")
for name, location in responses.items():
    print(f"{name} would like to go to {location}.")
