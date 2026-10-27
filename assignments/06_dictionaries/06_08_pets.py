peter = {
    'name': 'Peter Griffin',
    'species': 'Cat',
    'age': 5,
    'owner': 'Parker Santiago'
}

ozzie = {
    'name': 'Ozzie',
    'species': 'Cat',
    'age': 2,
    'owner': 'Adrian White'
}

ember = {
    'name': 'Ember',
    'species': 'Cat',
    'age': 3,
    'owner': 'Talan Crabill'
}

pets = [peter, ozzie, ember]

for pet in pets:
    print(f"Name: {pet['name']}")
    print(f"Species: {pet['species']}")
    print(f"Age: {pet['age']}")
    print(f"Owner: {pet['owner']}\n")