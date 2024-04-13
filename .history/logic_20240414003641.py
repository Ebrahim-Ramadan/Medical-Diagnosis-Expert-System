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
        global maximum_possible_diseases
        category, diseases_list = self.disease_categories[self.choice - 1]
        self.declare(Fact(disease=category))
        for dis in diseases_list:
            for symp in self.disease_symptoms[dis]:
                query = input(f"Do you have - {symp}?: ").strip()
                if query in ["Yes", "yes", "y", "Y"]:
                    self.possibilities[dis] = 1 + \
                        self.possibilities.get(dis, 0)

        max_value = max(self.possibilities.values())
        maximum_possible_diseases = []
        for key, value in self.possibilities.items():
            if value == max_value:
                maximum_possible_diseases.append(key)

        if len(maximum_possible_diseases) == 1:
            self.declare(Fact(probable_disease=maximum_possible_diseases[0]))
        elif len(maximum_possible_diseases) == 2:
            self.declare(Fact(probable_diseases=maximum_possible_diseases))

    @Rule(Fact(probable_disease=W()), salience=4)
    def matched(self):
        print(f"The most probable Disease is: {maximum_possible_diseases[0]}")

    @Rule(Fact(probable_diseases=W()), salience=4)
    def matched_diseases(self):
        print(f"The most probable Diseases are: {maximum_possible_diseases}")

    @Rule(NOT(Fact(probable_disease=W())), salience=4)
    def not_matched(self):
        print("Sorry Couldn't determine what is your most probable disease. \nYou can ask a real doctor for such case!\nOr you can diagnose in another specialization")
