# questions.py
import pytholog as pl

class MedicalQuestions:
    def __init__(self, knowledge_base):
        """
        Initialize medical questions with a knowledge base
        
        Args:
            knowledge_base (pl.KnowledgeBase): Existing knowledge base
        """
        self.kb = knowledge_base
    
    def get_symptom_questions(self):
        """
        Generate a list of symptom-related questions
        
        Returns:
            list: Symptom assessment questions
        """
        return [
            {
                "id": "fever_check",
                "question": "Are you experiencing fever?",
                "predicate": "symptom(john, fever)"
            },
            {
                "id": "headache_check", 
                "question": "Do you have a headache?",
                "predicate": "symptom(john, headache)"
            },
            {
                "id": "fatigue_check",
                "question": "Are you feeling unusually tired or fatigued?", 
                "predicate": "symptom(john, fatigue)"
            }
        ]
    
    def get_medical_history_questions(self):
        """
        Generate questions about medical history
        
        Returns:
            list: Medical history assessment questions
        """
        return [
            {
                "id": "diabetes_history",
                "question": "Do you have a history of diabetes?",
                "predicate": "history(john, diabetes)"
            },
            {
                "id": "hypertension_history",
                "question": "Have you been diagnosed with hypertension?",
                "predicate": "history(john, hypertension)"
            }
        ]
    
    def get_risk_assessment_questions(self):
        """
        Generate risk assessment questions
        
        Returns:
            list: Risk assessment questions
        """
        return [
            {
                "id": "diabetes_risk",
                "question": "Are you at risk for diabetes complications?",
                "predicate": "high_risk(john, diabetes_complications)"
            },
            {
                "id": "cardiovascular_risk",
                "question": "Are you at risk for cardiovascular issues?",
                "predicate": "high_risk(john, cardiovascular_risk)"
            }
        ]
    
    def interactive_questionnaire(self):
        """
        Conduct an interactive medical questionnaire
        
        Returns:
            dict: Collected patient information
        """
        patient_info = {}
        print("=== Medical Expert System Questionnaire ===")
        
        # Symptom Questions
        print("\n--- Symptom Assessment ---")
        for q in self.get_symptom_questions():
            response = input(f"{q['question']} (yes/no): ").lower()
            patient_info[q['id']] = response == 'yes'
            
            # If yes, add to knowledge base
            if response == 'yes':
                self.kb(q['predicate'])
        
        # Medical History Questions
        print("\n--- Medical History ---")
        for q in self.get_medical_history_questions():
            response = input(f"{q['question']} (yes/no): ").lower()
            patient_info[q['id']] = response == 'yes'
            
            # If yes, add to knowledge base
            if response == 'yes':
                self.kb(q['predicate'])
        
        return patient_info
    
    def generate_diagnosis(self, patient_info):
        """
        Generate potential diagnosis based on collected information
        
        Args:
            patient_info (dict): Collected patient information
        
        Returns:
            list: Potential diagnoses
        """
        diagnoses = []
        
        # Example diagnostic logic
        if patient_info.get('fever_check') and patient_info.get('fatigue_check'):
            diagnoses.append("Viral Infection")
        
        if patient_info.get('diabetes_history') and patient_info.get('fatigue_check'):
            diagnoses.append("Diabetes Complications")
        
        if patient_info.get('hypertension_history') and patient_info.get('headache_check'):
            diagnoses.append("Cardiovascular Risk")
        
        return diagnoses
    
    def recommend_treatment(self, diagnoses):
        """
        Recommend treatments based on diagnoses
        
        Args:
            diagnoses (list): List of potential diagnoses
        
        Returns:
            dict: Treatment recommendations
        """
        treatments = {}
        
        for diagnosis in diagnoses:
            if diagnosis == "Viral Infection":
                treatments[diagnosis] = [
                    "Get plenty of rest",
                    "Stay hydrated",
                    "Take over-the-counter fever reducers"
                ]
            
            if diagnosis == "Diabetes Complications":
                treatments[diagnosis] = [
                    "Consult with your endocrinologist",
                    "Monitor blood sugar levels",
                    "Review medication dosage"
                ]
            
            if diagnosis == "Cardiovascular Risk":
                treatments[diagnosis] = [
                    "Schedule a cardiology consultation",
                    "Monitor blood pressure",
                    "Consider lifestyle modifications"
                ]
        
        return treatments

def main():
    """
    Demonstration of the medical questionnaire system
    """
    # Create a knowledge base (you might want to import from your main system)
    kb = pl.KnowledgeBase("MedicalExpertSystem")
    
    # Initialize medical questions
    medical_questions = MedicalQuestions(kb)
    
    # Conduct interactive questionnaire
    patient_info = medical_questions.interactive_questionnaire()
    
    # Generate diagnosis
    diagnoses = medical_questions.generate_diagnosis(patient_info)
    print("\n=== Potential Diagnoses ===")
    for diagnosis in diagnoses:
        print(f"- {diagnosis}")
    
    # Recommend treatments
    treatments = medical_questions.recommend_treatment(diagnoses)
    print("\n=== Treatment Recommendations ===")
    for diagnosis, recommendations in treatments.items():
        print(f"\n{diagnosis} Treatment:")
        for recommendation in recommendations:
            print(f"- {recommendation}")

if __name__ == "__main__":
    main()