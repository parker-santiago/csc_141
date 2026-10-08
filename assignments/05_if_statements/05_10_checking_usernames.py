Users = ['Praknar', 'IllDeadeye101', 'Admin', 'adrianstired','Waterblock17']
New_users = ['praknar', 'YellowBalloon', 'AstralSpiff', 'adrianstired','LiquidChris']

for new_user in New_users:
    if new_user.lower() in [user.lower() for user in Users]:
        print(f"Sorry, the username '{new_user}' is already taken. Please choose a different username.")
    else:
        print(f"The username '{new_user}' is available.")