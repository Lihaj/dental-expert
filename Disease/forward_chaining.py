# forward_chaining.py
import pytholog as pl
from facts import MedicalFacts
from rules import MedicalRules

class ForwardChainingReasoner:
    def __init__(self):
        self.facts = MedicalFacts()
        self.rules = MedicalRules()
        self.kb = pl.KnowledgeBase("MedicalExpertSystem")
        
        # Load facts and rules
        self.kb(self.facts.get_knowledge_base())
        self.kb(self.rules.get_rules())

    def forward_chain(self, query):
        """
        Perform forward chaining to derive new facts
        
        Args:
            query (pl.Expr): The query to reason about
        
        Returns:
            list: List of derived facts or results
        """
        try:
            results = self.kb.query(query)
            
            print(f"Forward Chaining Results for {query}:")
            for result in results:
                print(f"Query Result: {result}")
            
            return results
        except Exception as e:
            print(f"Error in forward chaining: {e}")
            return []

    def derive_new_facts(self):
        """
        Demonstrate deriving new facts through forward chaining
        """
        print("Deriving New Facts:")
        
        # Example derivations using Pytholog expressions
        derivations = [
            pl.Expr("diagnose(john, X)"),
            pl.Expr("recommend_treatment(john, X)"),
            pl.Expr("potential_serious_condition(john)")
        ]
        
        for derivation in derivations:
            self.forward_chain(derivation)