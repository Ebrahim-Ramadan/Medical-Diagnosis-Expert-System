from experta import *


class knowledge(KnowledgeEngine):
    def __init__(self, disease_categories, disease_symptoms, choice):
        self.disease_categories = list(disease_categories.items())
        self.disease_symptoms = disease_symptoms
        self.choice = choice
        self.possibilities = {}
        super().__init__()

    @DefFacts()
    def _initial_action(self):
        yield Fact(choice=self.choice)
        yield Fact(action="diagnose")

    # Major upnormal organ. e.g: Ear, Nose, and Throat (ENT) Diseases
    @Rule(Fact(action="diagnose"), salience=5)
    def disease(self):
        category, diseases_list = self.disease_categories[self.choice]
        self.declare(Fact(disease=category))
        for dis in diseases_list:
            for symp in self.disease_symptoms[dis]:
                query = input(f"Do you have - {symp}?: ").strip()
                if query in ["Yes", "yes", "y", "Y"]:
                    self.possibilities[dis] = 1 + \
                        self.possibilities.get(dis, 0)
