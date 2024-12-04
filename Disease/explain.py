# explain.py
class MedicalExplanation:
    def __init__(self, patient_info, diagnoses, treatments):
        """
        Initialize explanation system
        
        Args:
            patient_info (dict): Patient's collected information
            diagnoses (list): Diagnosed conditions
            treatments (dict): Recommended treatments
        """
        self.patient_info = patient_info
        self.diagnoses = diagnoses
        self.treatments = treatments

    def explain_reasoning(self):
        """
        Provide a comprehensive explanation of the diagnostic reasoning
        """
        print("\n=== Diagnostic Reasoning Explanation ===")
        
        # Explain input facts
        self._explain_input_facts()
        
        # Explain diagnostic rules
        self._explain_diagnostic_rules()
        
        # Explain diagnoses
        self._explain_diagnoses()
        
        # Explain treatment recommendations
        self._explain_treatments()

    def _explain_input_facts(self):
        """
        Explain the input facts collected during the questionnaire
        """
        print("\n1. Patient Input Facts:")
        
        # Symptom facts
        symptom_facts = {
            'fever_check': 'Fever present',
            'headache_check': 'Headache reported',
            'fatigue_check': 'Fatigue experienced'
        }
        
        # Medical history facts
        history_facts = {
            'diabetes_history': 'History of Diabetes',
            'hypertension_history': 'History of Hypertension'
        }
        
        print("   Symptoms:")
        for key, description in symptom_facts.items():
            if self.patient_info.get(key):
                print(f"   - {description}")
        
        print("\n   Medical History:")
        for key, description in history_facts.items():
            if self.patient_info.get(key):
                print(f"   - {description}")

    def _explain_diagnostic_rules(self):
        """
        Explain the diagnostic reasoning rules
        """
        print("\n2. Diagnostic Reasoning Rules:")
        
        rules = [
            {
                "condition": "Fever + Fatigue",
                "explanation": "Combination of fever and fatigue typically indicates a viral infection",
                "logic": "If patient has fever and fatigue, potential viral infection is suspected"
            },
            {
                "condition": "Diabetes History + Fatigue",
                "explanation": "Fatigue in a patient with diabetes history may indicate diabetes complications",
                "logic": "Fatigue can be a sign of unmanaged diabetes or related metabolic issues"
            },
            {
                "condition": "Hypertension + Headache",
                "explanation": "Headache in a patient with hypertension history may suggest cardiovascular risk",
                "logic": "Headaches can be a symptom of high blood pressure or cardiovascular stress"
            }
        ]
        
        for rule in rules:
            print(f"   Rule: {rule['condition']}")
            print(f"   - {rule['explanation']}")
            print(f"   - Logical Reasoning: {rule['logic']}")

    def _explain_diagnoses(self):
        """
        Provide detailed explanations for each diagnosis
        """
        print("\n3. Diagnosis Explanations:")
        
        diagnosis_details = {
            "Viral Infection": {
                "key_indicators": ["Fever", "Fatigue"],
                "additional_info": "Viral infections are common and typically resolve with rest and hydration"
            },
            "Diabetes Complications": {
                "key_indicators": ["Diabetes History", "Fatigue"],
                "additional_info": "Ongoing fatigue may indicate need for diabetes management review"
            },
            "Cardiovascular Risk": {
                "key_indicators": ["Hypertension History", "Headache"],
                "additional_info": "Potential indicators of cardiovascular stress requiring medical attention"
            }
        }
        
        for diagnosis in self.diagnoses:
            if diagnosis in diagnosis_details:
                details = diagnosis_details[diagnosis]
                print(f"   {diagnosis}:")
                print("   - Key Indicators:")
                for indicator in details['key_indicators']:
                    print(f"     * {indicator}")
                print(f"   - {details['additional_info']}")

    def _explain_treatments(self):
        """
        Explain the reasoning behind treatment recommendations
        """
        print("\n4. Treatment Recommendation Reasoning:")
        
        treatment_reasoning = {
            "Viral Infection": {
                "primary_goal": "Manage symptoms and support recovery",
                "rationale": "Rest, hydration, and over-the-counter medications help the body fight viral infections"
            },
            "Diabetes Complications": {
                "primary_goal": "Stabilize blood sugar and prevent further complications",
                "rationale": "Requires medical consultation to adjust treatment plan and manage underlying condition"
            },
            "Cardiovascular Risk": {
                "primary_goal": "Reduce cardiovascular stress and prevent potential complications",
                "rationale": "Requires specialized medical assessment and potential lifestyle modifications"
            }
        }
        
        for diagnosis, treatments in self.treatments.items():
            if diagnosis in treatment_reasoning:
                reasoning = treatment_reasoning[diagnosis]
                print(f"   {diagnosis} Treatment:")
                print(f"   - Primary Goal: {reasoning['primary_goal']}")
                print(f"   - Rationale: {reasoning['rationale']}")
                print("   Recommended Actions:")
                for treatment in treatments:
                    print(f"   - {treatment}")

def create_explanation(patient_info, diagnoses, treatments):
    """
    Create and display a comprehensive medical reasoning explanation
    
    Args:
        patient_info (dict): Collected patient information
        diagnoses (list): Identified diagnoses
        treatments (dict): Recommended treatments
    """
    explanation = MedicalExplanation(patient_info, diagnoses, treatments)
    explanation.explain_reasoning()