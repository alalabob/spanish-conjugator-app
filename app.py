import streamlit as st

st.title("Spanish Verb Conjugator")

PRONOUNS = ["yo","tú","vos","él/ella/Ud.","nosotros","ellos/ellas/Uds."]

# -----------------------------
# IRREGULAR VERBS (MINIMAL SET)
# -----------------------------
IRREGULAR = {
    "ser": {
        "Present": ["soy","eres","sos","es","somos","son"],
        "Preterite": ["fui","fuiste","fuiste","fue","fuimos","fueron"],
        "Future": ["seré","serás","serás","será","seremos","serán"],
        "Conditional": ["sería","serías","serías","sería","seríamos","serían"]
    },
    "ir": {
        "Present": ["voy","vas","vas","va","vamos","van"],
        "Preterite": ["fui","fuiste","fuiste","fue","fuimos","fueron"]
    },
    "tener": {
        "Present": ["tengo","tienes","tenés","tiene","tenemos","tienen"]
    }
}

# -----------------------------
# REGULAR VERB ENGINE
# -----------------------------
def regular_conjugate(verb):
    stem = verb[:-2]
    ending = verb[-2:]

    if ending == "ar":
        return {
            "Present": [stem+"o", stem+"as", stem+"ás", stem+"a", stem+"amos", stem+"an"],
            "Preterite": [stem+"é", stem+"aste", stem+"aste", stem+"ó", stem+"amos", stem+"aron"],
            "Future": [verb+"é", verb+"ás", verb+"ás", verb+"á", verb+"emos", verb+"án"],
            "Conditional": [verb+"ía", verb+"ías", verb+"ías", verb+"ía", verb+"íamos", verb+"ían"]
        }

    if ending == "er":
        return {
            "Present": [stem+"o", stem+"es", stem+"és", stem+"e", stem+"emos", stem+"en"],
            "Preterite": [stem+"í", stem+"iste", stem+"iste", stem+"ió", stem+"imos", stem+"ieron"],
            "Future": [verb+"é", verb+"ás", verb+"ás", verb+"á", verb+"emos", verb+"án"],
            "Conditional": [verb+"ía", verb+"ías", verb+"ías", verb+"ía", verb+"íamos", verb+"ían"]
        }

    if ending == "ir":
        return {
            "Present": [stem+"o", stem+"es", stem+"ís", stem+"e", stem+"imos", stem+"en"],
            "Preterite": [stem+"í", stem+"iste", stem+"iste", stem+"ió", stem+"imos", stem+"ieron"],
            "Future": [verb+"é", verb+"ás", verb+"ás", verb+"á", verb+"emos", verb+"án"],
            "Conditional": [verb+"ía", verb+"ías", verb+"ías", verb+"ía", verb+"íamos", verb+"ían"]
        }

    return {}

# -----------------------------
# MAIN ENGINE
# -----------------------------
def conjugate(verb):
    verb = verb.lower().strip()

    if verb in IRREGULAR:
        return IRREGULAR[verb]

    return regular_conjugate(verb)

# -----------------------------
# UI
# -----------------------------
verb = st.text_input("Enter verb", "hablar")

if st.button("Generate"):
    data = conjugate(verb)

    st.subheader(f"Conjugation: {verb}")

    for tense, forms in data.items():
        st.markdown(f"## {tense}")

        cols = st.columns(len(PRONOUNS))
        for i, col in enumerate(cols):
            col.write(PRONOUNS[i])
            col.write(forms[i])
