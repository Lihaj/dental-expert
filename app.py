class DentalExpertSystem:
    def __init__(self):
        self.diseases = {
            "Cavities": {
                "symptoms": ["tooth pain", "sensitivity to sweets", "visible holes"],
                "detailed_questions": {
                    "tooth pain": [
                        "Do you experience sharp, sudden pain when biting down?",
                        "Does the pain worsen when eating hot or cold foods?",
                        "Do you feel persistent aching in a specific tooth?",
                        "Does the pain keep you awake at night?"
                    ],
                    "sensitivity to sweets": [
                        "Do you experience pain when eating sugary foods?",
                        "Do your teeth hurt when consuming cold or sweet drinks?",
                        "Do you feel a sharp sensation when something sweet touches your teeth?"
                    ],
                    "visible holes": [
                        "Have you noticed any dark spots or holes in your teeth?",
                        "Can you see any discoloration or chipped areas in your teeth?",
                        "When you run your tongue over your teeth, do you feel any rough or uneven surfaces?"
                    ]
                },
                "treatment": (
                    "\n* Dental fillings: Removing the decayed part and filling it with composite resin, amalgam, or other materials.\n"
                    "* Crowns: If the cavity is extensive, a crown may be used to protect the remaining tooth.\n"
                    "* Fluoride treatments: Strengthen enamel and reverse early stages of decay.\n"
                    "* Preventive care: Brushing twice daily with fluoride toothpaste, reducing sugary foods and drinks."
                )
            },
            "Tooth Sensitivity": {
                "symptoms": ["tooth pain", "sensitivity to sweets"],
                "detailed_questions": {
                    "tooth pain": [
                        "Do you experience sharp, quick pain when exposed to cold or hot temperatures?",
                        "Does brushing or flossing cause discomfort?",
                        "Do you experience pain when breathing in cold air?",
                        "Is the pain localized to a specific tooth or area?"
                    ],
                    "sensitivity to sweets": [
                        "Do sweet foods cause a sudden, sharp pain?",
                        "Do you avoid certain foods due to sensitivity?",
                        "Does the pain subside quickly after the stimulus is removed?"
                    ]
                },
                "treatment": (
                    "\n* Desensitizing toothpaste: Reduces nerve sensitivity over time.\n"
                    "* Fluoride treatments: Applied by a dentist to strengthen enamel and reduce pain.\n"
                    "* Dental bonding: Covers exposed roots or damaged areas with a protective resin.\n"
                    "* Nightguards: For teeth grinding (bruxism) which can exacerbate sensitivity."
                )
            },
            "Tooth Abscess": {
                "symptoms": ["tooth pain", "swollen gums", "bad breath"],
                "detailed_questions": {
                    "tooth pain": [
                        "Do you experience severe, throbbing pain?",
                        "Does the pain worsen when you lie down?",
                        "Do you feel pain when touching the affected area?",
                        "Is the pain constant or intermittent?"
                    ],
                    "swollen gums": [
                        "Are your gums red and swollen?",
                        "Do you notice any pus around the affected tooth?",
                        "Is there a painful bump or abscess on your gums?",
                        "Do your gums feel tender to touch?"
                    ],
                    "bad breath": [
                        "Do people comment on your bad breath?",
                        "Do you have a persistent bad taste in your mouth?",
                        "Does the bad breath persist even after brushing?",
                        "Do you notice an unpleasant odor when you exhale?"
                    ]
                },
                "treatment": (
                    "\n* Root canal therapy: Removes the infection and seals the tooth to prevent reinfection.\n"
                    "* Incision and drainage: Draining the abscess if necessary.\n"
                    "* Antibiotics: To control the infection if it has spread.\n"
                    "* Tooth extraction: In severe cases where the tooth cannot be saved."
                )
            },
            "Gingivitis": {
                "symptoms": ["bleeding gums", "swollen gums", "bad breath"],
                "detailed_questions": {
                    "bleeding gums": [
                        "Do your gums bleed when brushing or flossing?",
                        "Do you see blood on your toothbrush or dental floss?",
                        "Do your gums bleed easily when touched?",
                        "Do you notice bleeding when eating hard foods?"
                    ],
                    "swollen gums": [
                        "Are your gums puffy or enlarged?",
                        "Do your gums appear red instead of pink?",
                        "Do your gums feel tender or painful?",
                        "Do you notice any changes in gum texture?"
                    ],
                    "bad breath": [
                        "Do you have persistent bad breath?",
                        "Do people comment on an unpleasant odor from your mouth?",
                        "Does the bad breath continue even after brushing?",
                        "Do you have a constant bad taste in your mouth?"
                    ]
                },
                "treatment": (
                    "\n* Improved oral hygiene: Regular brushing and flossing.\n"
                    "* Professional dental cleaning: Remove plaque and tartar buildup.\n"
                    "* Antiseptic mouthwash: Reduces bacteria and inflammation.\n"
                    "* Antibiotics: In severe cases to control bacterial infection."
                )
            },
        }

    def confirm_disease(self):
        print("\nAvailable Diseases:")
        for disease in self.diseases.keys():
            print(f"- {disease}")

        suspected_disease = input("\nEnter the name of the disease you want to confirm: ").strip()

        if suspected_disease not in self.diseases:
            print("Disease not found in our database.")
            return

        disease_details = self.diseases[suspected_disease]
        symptoms = disease_details["symptoms"]

        # Track confirmed and unconfirmed symptoms
        confirmed_symptoms = []
        unconfirmed_symptoms = []

        # Initial symptom check
        for symptom in symptoms:
            response = input(f"Do you have the symptom: {symptom}? (y/n): ").strip().lower()
            if response == 'y':
                confirmed_symptoms.append(symptom)
            else:
                unconfirmed_symptoms.append(symptom)

        # If not all symptoms are confirmed, do deeper investigation
        if unconfirmed_symptoms:
            print("\nLet's do a more detailed investigation of your symptoms.")
            for symptom in unconfirmed_symptoms:
                # Check if detailed questions exist for this symptom
                if "detailed_questions" in disease_details and symptom in disease_details["detailed_questions"]:
                    detailed_questions = disease_details["detailed_questions"][symptom]

                    # Ask additional detailed questions
                    detailed_confirmations = 0
                    total_questions = len(detailed_questions)

                    print(f"\nAdditional questions about {symptom}:")
                    for question in detailed_questions:
                        detailed_response = input(f"{question} (y/n): ").strip().lower()
                        if detailed_response == 'y':
                            detailed_confirmations += 1

                    # If more than half of detailed questions are confirmed, consider the symptom confirmed
                    if detailed_confirmations > total_questions // 2:
                        confirmed_symptoms.append(symptom)

        # Final diagnosis
        if len(confirmed_symptoms) == len(symptoms):
            print(f"\nConfirmed: You have {suspected_disease}")
            print(f"Matching Symptoms: {', '.join(confirmed_symptoms)}")
            print("\nTreatment Options:")
            print(disease_details["treatment"])
        elif confirmed_symptoms:
            confidence = len(confirmed_symptoms) / len(symptoms)
            if confidence >= 0.5:
                print(f"\nMay Have: High probability of {suspected_disease}")
                print(f"Confirmed Symptoms: {', '.join(confirmed_symptoms)}")
                print("Recommendation: Consult a dental professional for a definitive diagnosis.")
            else:
                print(f"\nMay Have: Low probability of {suspected_disease}")
                print(f"Partially Confirmed Symptoms: {', '.join(confirmed_symptoms)}")
                print("Recommendation: Seek professional medical advice for accurate diagnosis.")
        else:
            print(f"\nVery low probability of {suspected_disease}")
            print("Recommendation: Consult a dental professional for a comprehensive examination.")

    def diagnose(self):
        user_symptoms = []
        print("\nPlease answer the following questions about your symptoms (yes/no).")
        for symptom in {"tooth pain", "sensitivity to sweets", "visible holes", "swollen gums", "bleeding gums",
                        "bad breath"}:
            response = input(f"Do you have {symptom}? (y/n): ").strip().lower()
            if response == 'y':
                user_symptoms.append(symptom)

        perfectly_matching = []
        partially_matching = []

        for disease, details in self.diseases.items():
            disease_symptoms = details["symptoms"]
            matched_symptoms = set(user_symptoms).intersection(disease_symptoms)
            if len(matched_symptoms) == len(disease_symptoms):
                perfectly_matching.append({
                    "name": disease,
                    "matched_count": len(matched_symptoms),
                    "symptoms": disease_symptoms,
                    "treatment": details["treatment"]
                })
            elif matched_symptoms:
                partially_matching.append({
                    "name": disease,
                    "matched_count": len(matched_symptoms),
                    "symptoms": disease_symptoms,
                    "treatment": details["treatment"]
                })

        if perfectly_matching:
            print("\nYou have these diseases:")
            for disease in perfectly_matching:
                print(f"- {disease['name']} (Symptoms Matched: {disease['matched_count']})")
                print(f"  Symptoms: {', '.join(disease['symptoms'])}")
                print(f"  Treatment: {disease['treatment']}\n")
        else:
            print("\nYou may have these diseases:")
            for disease in partially_matching:
                print(f"- {disease['name']} (Symptoms Matched: {disease['matched_count']})")
                print(f"  Symptoms: {', '.join(disease['symptoms'])}")
                print(f"  Treatment: {disease['treatment']}\n")


    def run(self):
        while True:
            print("Select an option:")
            print("1. Disease Diagnosis")
            print("2. Confirm Specific Disease")
            print("3. Exit")
            choice = input("Enter your choice (1, 2, 3): ").strip()

            if choice == '1':
                self.diagnose()
            elif choice == '2':
                self.confirm_disease()
            elif choice == '3':
                print("Thank you for using the Dental Expert System. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    expert_system = DentalExpertSystem()
    expert_system.run()