from experta import *


class RangeError(Exception):
    def __init__(self, message):
        self.message = message


def validate_Choice(choice):
    if (choice < 1 or choice > 10):
        raise RangeError("Choice out of range")


class knowledge(KnowledgeEngine):
    def __init__(self, disease_categories, disease_symptoms):
        self.disease_categories = disease_categories
        self.disease_symptoms = disease_symptoms
        super().__init__()

    @DefFacts()
    def _initial_action(self):

        yield Fact(choice=1)
