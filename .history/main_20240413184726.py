import json
from logic import knowledge

# Handleing some user unexpected errors


class RangeError(Exception):
    def __init__(self, message):
        self.message = message


def validate_Choice(choice):
    if (choice < 1 or choice > 10):
        raise RangeError("Choice out of range.\nChoose from (1 - 10)")


def choose_diagnose():
    try:
        try:
            choose = int(input("""
                        Welcome to Medical diagnosis expert system.

                        Specify which organ or specialization you would like to diagnose

                        1. Ear, Nose, and Throat (ENT) Diseases
                        2. Dental and Oral Diseases
                        3. Musculoskeletal Diseases
                        4. Cardiopulmonary Diseases
                        5. Gastrointestinal Diseases
                        6. Neurological Diseases
                        7. Endocrine Diseases
                        8. Urogenital Diseases
                        9. Ophthalmic Diseases
                        10. Dermatological Diseases

                        Choose from (1 - 10)
                        """))
            validate_Choice(choose)
            return choose
        except RangeError as e:
            print(e.message)
    except ValueError:
        print("Only Integer numbers are valid")


def processs_data():
    global disease_categories
    global disease_symptoms
    with open('disease_categories.json', 'r') as file:
        disease_categories = json.load(file)

    with open('disease_symptoms.json', 'r') as file:
        disease_symptoms = json.load(file)


if __name__ == "__main__":
    processs_data()
    while True:
        choose = choose_diagnose()
        engine = knowledge(disease_categories, disease_symptoms, choose)
        engine.reset()
        engine.run()
        answer = input("Diagnoes again?(Y/N): ").strip()
        if answer in ['No', 'N', 'no', 'n']:
            exit()
