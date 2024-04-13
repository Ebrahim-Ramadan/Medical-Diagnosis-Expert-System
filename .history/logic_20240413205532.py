from experta import *


class knowledge(KnowledgeEngine):
    def __init__(self, disease_categories, disease_symptoms, choose):
        self.disease_categories = list(disease_categories)
        self.disease_symptoms = disease_symptoms
        self.choose = choose
        super().__init__()

    @DefFacts()
    def _initial_action(self):
        yield Fact(choice=self.choose)

    @Rule(Fact(choice=1), salience=5)  # Ear, Nose, and Throat (ENT) Diseases
    def disease_1(self):
