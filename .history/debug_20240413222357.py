from main import *
possibilities = {}

category, diseases_list = disease_categories[0]
for dis in diseases_list:
    for symp in disease_symptoms[dis]:
        query = input(f"Do you have - {symp}?: ").strip()
        if query in ["Yes", "yes", "y", "Y"]:
            possibilities[dis] = 1 + possibilities.get(dis, 0)

print(possibilities)
