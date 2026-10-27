rivers = {
    "Nile": "Egypt",
    "Amazon": "Brazil",
    "Yangtze": "China",
    }

for river, country in rivers.items():
    print(f"The {river} runs through {country}.")

print("\nList of rivers:")
for river in rivers.keys():
    print(river)

print("\nList of countries:")
for country in rivers.values():
    print(country)