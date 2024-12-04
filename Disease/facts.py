# facts.py
import pytholog as pl

class MedicalFacts:
    def __init__(self):
        self.patient_facts = [
            "age(john, 45)",
            "gender(john, male)",
            "weight(john, 80)",
            "height(john, 175)"
        ]

        # Symptom-related facts
        self.symptom_facts = [
            "symptom(john, fever)",
            "symptom(john, headache)",
            "symptom(john, fatigue)",
            "fever_duration(john, 3)"  # Changed from duration to fever_duration
        ]

        # Medical history facts
        self.medical_history_facts = [
            "history(john, diabetes)",
            "history(john, hypertension)",
            "medication(john, insulin)",
            "medication(john, blood_pressure_medication)"
        ]

    def get_knowledge_base(self):
        """
        Combine all fact categories into a single knowledge base
        """
        return (
            self.patient_facts + 
            self.symptom_facts + 
            self.medical_history_facts
        )