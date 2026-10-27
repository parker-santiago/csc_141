John_Pork = {
    'first_name': 'John',
    'last_name': 'Pork',
    'age': 25,
    'city': 'Cleveland'
}

Parker_Santiago = {
    'first_name': 'Parker',
    'last_name': 'Santiago',
    'age': 19,
    'city': 'Wilmington'
}

Chris_Chan = {
    'first_name': 'Christian',
    'last_name': 'Chandler',
    'age': 44,
    'city': 'cwcvill'
}

people = [John_Pork, Parker_Santiago, Chris_Chan]

for person in people:
    print(f"First Name: {person['first_name']}")
    print(f"Last Name: {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"City: {person['city']}\n")