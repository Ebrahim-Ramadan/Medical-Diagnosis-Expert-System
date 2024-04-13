import json
from logic import knowledge

with open('disease_categories.json', 'r') as file:
    disease_categories = json.load(file)

with open('disease_symptoms.json', 'r') as file:
    disease_symptoms = json.load(file)

if __name__ == "__main__":
    engine = knowledge(disease_categories, disease_symptoms)
    while True:
        engine.reset()
        engine.run()
        answer = input("Diagnoes again?(Y/N): ")
        if answer in ['No', 'N', 'no', 'n']:
            exit()
