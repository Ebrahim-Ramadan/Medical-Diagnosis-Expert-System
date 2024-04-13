from experta import *


class knowledge(KnowledgeEngine):
    def __init__(self, disease_categories, disease_symptoms, choose):
        self.disease_categories = list(disease_categories)
        self.disease_symptoms = list(disease_symptoms)
        self.choose = choose
        super().__init__()

    @DefFacts()
    def _initial_action(self):
        yield Fact(choice=self.choose)
        yield Fact(action="diagnose")

    # Ear, Nose, and Throat (ENT) Diseases
    @Rule(Fact(action="diagnose"), salience=5)
    def disease(self):
        pass
