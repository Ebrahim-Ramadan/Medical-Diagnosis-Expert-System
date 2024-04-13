from experta import *


class knowledge(KnowledgeEngine):
    def __init__(self, disease_categories, disease_symptoms):
        self.disease_categories = disease_categories
        self.disease_symptoms = disease_symptoms
        super().__init__()

    @DefFacts()
    def _initial_action(self):
        print("""
specify which organ or specialization you would like to Diagnose
              hello world
        """)
        yield Fact(action="start")
