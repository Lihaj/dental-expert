
import pytholog as pl
from forward_chaining import ForwardChainingReasoner
from backward_chaining import BackwardChainingReasoner
from questions import MedicalQuestions
from explain import create_explanation

class MedicalExpertSystem:
    def __init__(self):
        self.forward_reasoner = ForwardChainingReasoner()
        self.backward_reasoner = BackwardChainingReasoner()
        self.kb = self.forward_reasoner.kb  # Use the same knowledge base
        self.medical_questions = MedicalQuestions(self.kb)

    def run_diagnostic_process(self):
        """
        Run full diagnostic process with explanation
        """
        # Conduct interactive questionnaire
        patient_info = self.medical_questions.interactive_questionnaire()
        
        # Generate diagnosis
        diagnoses = self.medical_questions.generate_diagnosis(patient_info)
        print("\n=== Potential Diagnoses ===")
        for diagnosis in diagnoses:
            print(f"- {diagnosis}")
        
        # Recommend treatments
        treatments = self.medical_questions.recommend_treatment(diagnoses)
        print("\n=== Treatment Recommendations ===")
        for diagnosis, recommendations in treatments.items():
            print(f"\n{diagnosis} Treatment:")
            for recommendation in recommendations:
                print(f"- {recommendation}")
        
        # Generate explanation
        create_explanation(patient_info, diagnoses, treatments)

    def interactive_forward_chaining(self):
        """
        Interactive forward chaining with user-defined queries
        """
        print("\n=== Interactive Forward Chaining ===")
        print("Available Predicate Examples:")
        print("- diagnose(john, X)")
        print("- recommend_treatment(john, X)")
        print("- high_risk(john, X)")
        print("- potential_serious_condition(john)")
        print("\nEnter 'quit' to return to main menu")

        while True:
            # Get user query
            query_str = input("\nEnter a forward chaining query (use X for variables): ").strip()
            
            # Check for quit
            if query_str.lower() == 'quit':
                break

            try:
                # Convert string to Pytholog expression
                query = pl.Expr(query_str)
                
                # Perform forward chaining
                print(f"\nForward Chaining Query: {query}")
                results = self.forward_reasoner.forward_chain(query)
                
                # Check if no results found
                if not results:
                    print("No results found for this query.")
            
            except Exception as e:
                print(f"Error processing query: {e}")
                print("Please check your query syntax.")

    def interactive_backward_chaining(self):
        """
        Interactive backward chaining with user-defined queries
        """
        print("\n=== Interactive Backward Chaining ===")
        print("Available Predicate Examples:")
        print("- diagnose(john, viral_infection)")
        print("- high_risk(john, diabetes_complications)")
        print("- recommend_treatment(john, rest_and_hydration)")
        print("\nEnter 'quit' to return to main menu")

        while True:
            # Get user query
            query_str = input("\nEnter a backward chaining query: ").strip()
            
            # Check for quit
            if query_str.lower() == 'quit':
                break

            try:
                # Convert string to Pytholog expression
                query = pl.Expr(query_str)
                
                # Perform backward chaining
                print(f"\nBackward Chaining Query: {query}")
                results = self.backward_reasoner.backward_chain(query)
                
                # Check if no results found
                if not results:
                    print("No results found for this query.")
            
            except Exception as e:
                print(f"Error processing query: {e}")
                print("Please check your query syntax.")

def main():
    print("Medical Expert System - Interactive Interface")
    print("---------------------")
    print("Menu Options:")
    print("1. Run Medical Diagnosis")
    print("2. Interactive Forward Chaining")
    print("3. Interactive Backward Chaining")
    print("4. Predefined Forward Chaining Demonstration")
    print("5. Predefined Backward Chaining Demonstration")
    print("6. Exit")

    expert_system = MedicalExpertSystem()

    while True:
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == '1':
            # Run full diagnostic process with explanation
            expert_system.run_diagnostic_process()
        
        elif choice == '2':
            # Interactive forward chaining
            expert_system.interactive_forward_chaining()
        
        elif choice == '3':
            # Interactive backward chaining
            expert_system.interactive_backward_chaining()
        
        elif choice == '4':
            # Predefined forward chaining demonstration
            print("\n=== Predefined Forward Chaining Demonstration ===")
            queries = [
                pl.Expr("diagnose(john, X)"),
                pl.Expr("recommend_treatment(john, X)"),
                pl.Expr("potential_serious_condition(john)")
            ]
            for query in queries:
                print(f"\nForward Chaining Query: {query}")
                expert_system.forward_reasoner.forward_chain(query)
        
        elif choice == '5':
            # Predefined backward chaining demonstration
            print("\n=== Predefined Backward Chaining Demonstration ===")
            queries = [
                pl.Expr("diagnose(john, viral_infection)"),
                pl.Expr("high_risk(john, diabetes_complications)"),
                pl.Expr("recommend_treatment(john, rest_and_hydration)")
            ]
            for query in queries:
                print(f"\nBackward Chaining Query: {query}")
                expert_system.backward_reasoner.backward_chain(query)
        
        elif choice == '6':
            print("Exiting Medical Expert System. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()