# backward_chaining.py
import pytholog as pl
from facts import MedicalFacts
from rules import MedicalRules

class BackwardChainingReasoner:
    def __init__(self):
        self.facts = MedicalFacts()
        self.rules = MedicalRules()
        self.kb = pl.KnowledgeBase("MedicalExpertSystem")
        
        # Load facts and rules
        self.kb(self.facts.get_knowledge_base())
        self.kb(self.rules.get_rules())

    def backward_chain(self, query):
        """
        Perform backward chaining to prove a hypothesis
        
        Args:
            query (pl.Expr): The hypothesis to prove
        
        Returns:
            list: List of proofs or results
        """
        try:
            results = self.kb.query(query)
            
            print(f"Backward Chaining Results for {query}:")
            for result in results:
                print(f"Hypothesis Proof: {result}")
            
            return results
        except Exception as e:
            print(f"Error in backward chaining: {e}")
            return []

    def test_hypotheses(self):
        """
        Test various medical hypotheses using backward chaining
        """
        print("Testing Medical Hypotheses:")
        
        # Example hypotheses using Pytholog expressions
        hypotheses = [
            pl.Expr("diagnose(john, viral_infection)"),
            pl.Expr("high_risk(john, diabetes_complications)"),
            pl.Expr("recommend_treatment(john, rest_and_hydration)")
        ]
        
        for hypothesis in hypotheses:
            self.backward_chain(hypothesis)