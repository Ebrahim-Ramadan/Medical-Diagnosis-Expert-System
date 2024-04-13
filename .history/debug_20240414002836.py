import json


def processs_data():
    global disease_categories
    global disease_symptoms
    with open('disease_categories.json', 'r') as file:
        disease_categories = json.load(file)

    with open('disease_symptoms.json', 'r') as file:
        disease_symptoms = json.load(file)


processs_data()
possibilities = {}
disease_categories = list(disease_categories.items())
category, diseases_list = disease_categories[0]
print(disease_symptoms["Otitis media (middle ear infection)"])
print(diseases_list)
for dis in diseases_list:
    for symp in disease_symptoms[dis]:  # The error is here key error
        query = input(f"Do you have - {symp}?: ").strip()
        if query in ["Yes", "yes", "y", "Y"]:
            possibilities[dis] = 1 + possibilities.get(dis, 0)

max_value = possibilities.values()
maximum_possible_diseases = []
for key, value in possibilities.items():
    if value == max_value:
        maximum_possible_diseases.append(key)

if len(maximum_possible_diseases) == 1:
    print("the possible disease: ", maximum_possible_diseases[0])
elif len(maximum_possible_diseases) == 2:
    print("the possible diseases: ", maximum_possible_diseases)
