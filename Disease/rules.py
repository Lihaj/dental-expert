# rules.py
import pytholog as pl

class MedicalRules:
    def __init__(self):
        # Define medical diagnosis rules
        self.rules = [
            # Fever-related rules with explicit condition handling
            "diagnose(X, viral_infection) :- symptom(X, fever), symptom(X, fatigue), fever_duration(X, Days), Days > 2",
            
            # Risk assessment rules
            "high_risk(X, diabetes_complications) :- history(X, diabetes), symptom(X, fatigue)",
            "high_risk(X, cardiovascular_risk) :- history(X, hypertension), age(X, Age), Age > 40",
            
            # Treatment recommendation rules
            "recommend_treatment(X, rest_and_hydration) :- diagnose(X, viral_infection)",
            "recommend_treatment(X, medical_consultation) :- high_risk(X, diabetes_complications)",
            
            # Complex diagnostic rule
            "potential_serious_condition(X) :- high_risk(X, cardiovascular_risk), symptom(X, headache)"
        ]

    def get_rules(self):
        """
        Return the defined medical rules
        """
        return self.rules