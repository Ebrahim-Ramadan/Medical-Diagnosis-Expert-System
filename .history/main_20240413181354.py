import json
from logic import knowledge


class RangeError(Exception):
    def __init__(self, message):
        self.message = message


def validate_Choice(choice):
    if (choice < 1 or choice > 10):
        raise RangeError("Choice out of range.\nChoose from (1 - 10)")


with open('disease_categories.json', 'r') as file:
    disease_categories = json.load(file)

with open('disease_symptoms.json', 'r') as file:
    disease_symptoms = json.load(file)

if __name__ == "__main__":
    engine = knowledge(disease_categories, disease_symptoms)
    while True:
        engine.reset()
        engine.run()
        answer = input("Diagnoes again?(Y/N): ").strip()
        if answer in ['No', 'N', 'no', 'n']:
            exit()
