people = ["Gordon Ramsey", "Gabe Newell", "Talan Crabill"]

print(f"You, {people[0]}, are invited to my dinner party! (to cook for me)")
print(f"Dearest {people[1]}, I would be honored if you could attend my dinner party! I already have head chef Ramsey preparing the food, so you can just relax and enjoy the meal.")
print(f"{people[2]}, I somehow have multiple celebrities coming to my house for dinner. GET YOUR ASS OVER HERE NOW")

cancelled_guest = people.pop(0)

print(f"\nUnfortunately, {cancelled_guest} has cancelled on me. I guess I'll have to find a new chef for my dinner party.\n")

people.insert(0, "Ronald McDonald")

print(f"You, {people[0]}, are invited to my dinner party! (to cook for me)")
print(f"Dearest {people[1]}, I would be honored if you could attend my dinner party! Unfortunately, Chef Ramsey has cancelled, though we were able to sub him out for Ronald McDonald!")
print(f"{people[2]}, Gabe Newell and Ronald McDonald are coming to my house for dinner. Get here now. This will be huge.")