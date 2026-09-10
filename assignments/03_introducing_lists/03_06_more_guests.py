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

print("\nI just found a bigger table for my dinner party, so I can invite more people!\n")

people.insert(0, "Parappa the Rapper")
people.insert(2, "Tyler the Creator")
people.append("Wall-E")

print(f"{people[0]}, you're invited to come eat at my dinner party! You can bring Sunny Funny if you want but she'll have to bring her own chair.")
print(f"You, {people[1]}, are invited to my dinner party! (to cook for me)")
print(f"{people[2]}, I want you at my dinner party tomorrow night! I know you have a busy schedule, but you wont regret attending this event.")
print(f"Dearest {people[3]}, I would be honored if you could attend my dinner party! Unfortunately, Chef Ramsey has cancelled, though we were able to sub him out for Ronald McDonald!")
print(f"{people[4]}, Like everybody is coming to my house for dinner. Get here now. This will be huge.")
print(f"Hello {people[5]}! I know you can't really eat but I still want you at my dinner party tomorrow night.")