group = input("How many people are in your group? ")
if int(group) > 8:
    print("I'm sorry, but we can't accommodate groups larger than 8 people.")
elif int(group) == 1:
    print(f"Your group of {group} person can be seated.")
else:
    print(f"Your group of {group} people can be seated.")