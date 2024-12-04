import streamlit as st
from experta import KnowledgeEngine, Fact, Rule, DefFacts, MATCH


class DentalExpertSystem(KnowledgeEngine):
    def __init__(self, diseases):
        super().__init__()
        self.diseases = diseases
        self.symptom_query = None
        self.confirmed_symptoms = []
        self.diagnosis_step = None
        self.current_disease = None

    @DefFacts()
    def _initial_action(self):
        yield Fact(action="start")

    def ask_symptom(self):
        if self.symptom_query:
            symptom = self.symptom_query.pop(0)
            return symptom
        return None

    def finalize_diagnosis(self):
        user_symptoms = set(self.confirmed_symptoms)
        perfectly_matching = []
        partially_matching = []

        for disease, details in self.diseases.items():
            disease_symptoms = set(details["symptoms"])
            matched_symptoms = user_symptoms.intersection(disease_symptoms)
            if len(matched_symptoms) == len(disease_symptoms):
                perfectly_matching.append({
                    "name": disease,
                    "symptoms": matched_symptoms,
                    "treatment": details["treatment"]
                })
            elif matched_symptoms:
                partially_matching.append({
                    "name": disease,
                    "symptoms": matched_symptoms,
                    "treatment": details["treatment"]
                })

        if perfectly_matching:
            return f"You have these diseases:\n" + "\n".join(
                f"- {d['name']} (Symptoms Matched: {len(d['symptoms'])})\nSymptoms: {', '.join(d['symptoms'])}\nTreatment: {d['treatment']}"
                for d in perfectly_matching)
        elif partially_matching:
            return f"You may have these diseases:\n" + "\n".join(
                f"- {d['name']} (Symptoms Matched: {len(d['symptoms'])})\nSymptoms: {', '.join(d['symptoms'])}\nTreatment: {d['treatment']}"
                for d in partially_matching)
        else:
            return "No diseases match your symptoms. Please consult a dentist for further advice."


# Define diseases, symptoms, detailed questions, and treatments
diseases = {
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

# Streamlit Interface
st.title("🦷 Dental Expert System Chatbot")
if "engine" not in st.session_state:
    st.session_state.engine = DentalExpertSystem(diseases)
    st.session_state.engine.reset()
    st.session_state.step = "start"

engine = st.session_state.engine

if "conversation" not in st.session_state:
    st.session_state.conversation = []

# Display chat history
for msg in st.session_state.conversation:
    st.chat_message(msg["role"]).write(msg["content"])

# Get user input
if prompt := st.chat_input("Type your response here..."):
    # Add user's response to the conversation
    st.session_state.conversation.append({"role": "user", "content": prompt})

    # Expert system logic
    if st.session_state.step == "start":
        st.session_state.conversation.append({
            "role": "assistant",
            "content": "Please answer the following questions about your symptoms (yes/no)."
        })
        st.session_state.step = "symptom_check"

    elif st.session_state.step == "symptom_check":
        symptoms = [
            "Do you have bleeding gums?",
            "Do you have visible holes?",
            "Do you have swollen gums?",
            "Do you have sensitivity to sweets?",
            "Do you have bad breath?",
            "Do you have tooth pain?"
        ]
        if symptoms:
            question = symptoms.pop(0)
            st.session_state.conversation.append({
                "role": "assistant",
                "content": question
            })
            st.session_state.step = "diagnosis"

    elif st.session_state.step == "diagnosis":
        user_input = prompt.lower()
        if user_input == 'y':
            engine.confirmed_symptoms.append(symptoms[0])  # Add the confirmed symptom

        # If no symptom matches, finalize diagnosis
        st.session_state.conversation.append({
            "role": "assistant",
            "content": engine.finalize_diagnosis()})

        st.session_state.step = "end"
