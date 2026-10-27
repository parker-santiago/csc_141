favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}

people = ['jen', 'sarah', 'parker', 'edward', 'phil', 'john']

for name in people:
    if name in favorite_languages:
        print(f"{name.title()} has already taken the poll and prefers {favorite_languages[name]}.")
    else:
        print(f"{name.title()} has not taken the poll yet.")