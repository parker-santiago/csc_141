Favorite_Numbers = {
    'Parker': [7, 64],
    'Adrian': [13, 26],
    'Talan': [21, 55],
    'Sonnie': [64, 42],
    "John Pork": [69, 67]
}

for name, numbers in Favorite_Numbers.items():
    print(f"{name}'s favorite numbers are:")
    for number in numbers:
        print(f"- {number}")