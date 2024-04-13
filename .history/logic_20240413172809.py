from experta import *


class knowledge(KnowledgeEngine):
    def __init__(self, disease_categories, disease_symptoms):
        self.disease_categories = disease_categories
        self.disease_symptoms = disease_symptoms
        super().__init__()

    @DefFacts()
    def _initial_action(self):
        print("""
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
            """)
        yield Fact(action="start")
