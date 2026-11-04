prompt = "Please enter a pizza topping: "
prompt += "Enter 'quit' to stop adding toppings. "
active = True
toppings = []
while active:
    topping = input(prompt)
    if topping == 'quit':
        active = False
    else:
        print(f"Adding {topping} to your pizza.")
        toppings.append(topping)
print("Your pizza will have the following toppings:")
for topping in toppings:
    print(f"\n- {topping}")