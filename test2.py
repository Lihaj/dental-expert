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
                f"- {d['name']} (Treatment: {d['treatment']})" for d in perfectly_matching)
        elif partially_matching:
            return f"You may have these diseases:\n" + "\n".join(
                f"- {d['name']} (Symptoms Matched: {', '.join(d['symptoms'])})\n  Treatment: {d['treatment']}"
                for d in partially_matching)
        else:
            return "No diseases match your symptoms. Please consult a dentist for further advice."


# Define diseases, symptoms, and treatments
diseases = {
    "Cavities": {
        "symptoms": ["tooth pain", "sensitivity to sweets", "visible holes"],
        "treatment": "Dental fillings, crowns, fluoride treatments."
    },
    "Tooth Sensitivity": {
        "symptoms": ["tooth pain", "sensitivity to sweets"],
        "treatment": "Desensitizing toothpaste, fluoride treatments, dental bonding."
    },
    "Tooth Abscess": {
        "symptoms": ["tooth pain", "swollen gums", "bad breath"],
        "treatment": "Root canal, antibiotics, incision, and drainage."
    },
    "Gingivitis": {
        "symptoms": ["bleeding gums", "swollen gums", "bad breath"],
        "treatment": "Improved oral hygiene, professional cleaning, antiseptic mouthwash."
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
            "content": "Do you want to 'diagnosis' or 'confirm'?"
        })
        st.session_state.step = "action_selection"

    elif st.session_state.step == "action_selection":
        if prompt.lower() == "diagnosis":
            engine.diagnosis_step = "symptom_check"
            engine.symptom_query = [
                "tooth pain", "sensitivity to sweets", "visible holes", "swollen gums", "bleeding gums", "bad breath"
            ]
            symptom = engine.ask_symptom()
            st.session_state.conversation.append({
                "role": "assistant",
                "content": f"Do you have {symptom}? (yes or no)"
            })
            st.session_state.step = "diagnosis"

        elif prompt.lower() == "confirm":
            st.session_state.conversation.append({
                "role": "assistant",
                "content": "Please enter the disease name you want to confirm:"
            })
            st.session_state.step = "confirm_disease"

        else:
            st.session_state.conversation.append({
                "role": "assistant",
                "content": "Invalid input. Please choose 'diagnosis' or 'confirm'."
            })

    elif st.session_state.step == "diagnosis":
        if prompt.lower() == "yes":
            engine.confirmed_symptoms.append(engine.symptom_query[0])

        symptom = engine.ask_symptom()
        if symptom:
            st.session_state.conversation.append({
                "role": "assistant",
                "content": f"Do you have {symptom}? (yes or no)"
            })
        else:
            diagnosis_result = engine.finalize_diagnosis()
            st.session_state.conversation.append({
                "role": "assistant",
                "content": diagnosis_result
            })
            st.session_state.step = "start"

    elif st.session_state.step == "confirm_disease":
        disease = prompt.strip()
        if disease in diseases:
            symptoms = diseases[disease]["symptoms"]
            treatment = diseases[disease]["treatment"]
            st.session_state.conversation.append({
                "role": "assistant",
                "content": f"'{disease}' has these symptoms: {', '.join(symptoms)}\nTreatment: {treatment}"
            })
        else:
            st.session_state.conversation.append({
                "role": "assistant",
                "content": f"Disease '{disease}' not found in our database."
            })
        st.session_state.step = "start"

    # Update conversation history
    for msg in st.session_state.conversation:
        st.chat_message(msg["role"]).write(msg["content"])
