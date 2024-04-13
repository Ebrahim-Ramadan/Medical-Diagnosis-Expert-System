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
print disease_symptoms("Otitis media (middle ear infection)")
# for dis in diseases_list:
#     for symp in disease_symptoms[dis]:
#         query = input(f"Do you have - {symp}?: ").strip()
#         if query in ["Yes", "yes", "y", "Y"]:
#             possibilities[dis] = 1 + possibilities.get(dis, 0)

# print(possibilities)
