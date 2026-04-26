PRONOUNS = ["yo","tú","vos","él/ella/Ud.","nosotros","ellos/ellas/Uds."]

# -----------------------------
# IRREGULAR VERBS (START SET)
# -----------------------------
IRREGULAR = {
    "ser": {
        "present": ["soy","eres","sos","es","somos","son"],
        "preterite": ["fui","fuiste","fuiste","fue","fuimos","fueron"],
        "future": ["seré","serás","serás","será","seremos","serán"],
        "conditional": ["sería","serías","serías","sería","seríamos","serían"]
    },
    "ir": {
        "present": ["voy","vas","vas","va","vamos","van"],
        "preterite": ["fui","fuiste","fuiste","fue","fuimos","fueron"]
    },
    "tener": {
        "present": ["tengo","tienes","tenés","tiene","tenemos","tienen"]
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
            "present": [stem+"o", stem+"as", stem+"ás", stem+"a", stem+"amos", stem+"an"],
            "preterite": [stem+"é", stem+"aste", stem+"aste", stem+"ó", stem+"amos", stem+"aron"],
            "future": [verb+"é", verb+"ás", verb+"ás", verb+"á", verb+"emos", verb+"án"],
            "conditional": [verb+"ía", verb+"ías", verb+"ías", verb+"ía", verb+"íamos", verb+"ían"]
        }

    if ending == "er":
        return {
            "present": [stem+"o", stem+"es", stem+"és", stem+"e", stem+"emos", stem+"en"],
            "preterite": [stem+"í", stem+"iste", stem+"iste", stem+"ió", stem+"imos", stem+"ieron"],
            "future": [verb+"é", verb+"ás", verb+"ás", verb+"á", verb+"emos", verb+"án"],
            "conditional": [verb+"ía", verb+"ías", verb+"ías", verb+"ía", verb+"íamos", verb+"ían"]
        }

    if ending == "ir":
        return {
            "present": [stem+"o", stem+"es", stem+"ís", stem+"e", stem+"imos", stem+"en"],
            "preterite": [stem+"í", stem+"iste", stem+"iste", stem+"ió", stem+"imos", stem+"ieron"],
            "future": [verb+"é", verb+"ás", verb+"ás", verb+"á", verb+"emos", verb+"án"],
            "conditional": [verb+"ía", verb+"ías", verb+"ías", verb+"ía", verb+"íamos", verb+"ían"]
        }

    return {}

# -----------------------------
# MAIN ENGINE
# -----------------------------
def conjugate(verb):
    verb = verb.lower()

    if verb in IRREGULAR:
        return IRREGULAR[verb]

    return regular_conjugate(verb)
