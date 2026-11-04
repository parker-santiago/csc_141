prompt = "Please enter your age: "
age = input(prompt)
if int(age) < 3:
    print("Your ticket is free.")
elif int(age) <= 12:
    print("Your ticket costs $10.")
else:
    print("Your ticket costs $15.")