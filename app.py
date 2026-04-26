# Rioplatense Spanish Conjugator - Version 1
# Indicative only (Present, Imperfect, Preterite, Future, Conditional)
# Supports: tú + vos, no vosotros

IRREGULARS = {
    "ser": {
        "present": {
            "yo": "soy",
            "tu": "eres",
            "vos": "sos",
            "usted": "es",
            "el_ella": "es",
            "nosotros": "somos",
            "ustedes": "son",
            "ellos": "son",
        }
    },
    "ir": {
        "present": {
            "yo": "voy",
            "tu": "vas",
            "vos": "vas",
            "usted": "va",
            "el_ella": "va",
            "nosotros": "vamos",
            "ustedes": "van",
            "ellos": "van",
        }
    },
    "tener": {
        "present": {
            "yo": "tengo",
            "tu": "tienes",
            "vos": "tenés",
            "usted": "tiene",
            "el_ella": "tiene",
            "nosotros": "tenemos",
            "ustedes": "tienen",
            "ellos": "tienen",
        }
    }
}

PRONOUNS = [
    "yo",
    "tu",
    "vos",
    "usted",
    "el_ella",
    "nosotros",
    "ustedes",
    "ellos",
]


def get_verb_type(verb):
    if verb.endswith("ar"):
        return "ar"
    if verb.endswith("er"):
        return "er"
    if verb.endswith("ir"):
        return "ir"
    return None


def get_stem(verb):
    return verb[:-2]


PRESENT_ENDINGS = {
    "ar": {
        "yo": "o",
        "tu": "as",
        "vos": "ás",
        "usted": "a",
        "el_ella": "a",
        "nosotros": "amos",
        "ustedes": "an",
        "ellos": "an",
    },
    "er": {
        "yo": "o",
        "tu": "es",
        "vos": "és",
        "usted": "e",
        "el_ella": "e",
        "nosotros": "emos",
        "ustedes": "en",
        "ellos": "en",
    },
    "ir": {
        "yo": "o",
        "tu": "es",
        "vos": "ís",
        "usted": "e",
        "el_ella": "e",
        "nosotros": "imos",
        "ustedes": "en",
        "ellos": "en",
    },
}


IMPERFECT_ENDINGS = {
    "ar": {
        "yo": "aba",
        "tu": "abas",
        "vos": "abas",
        "usted": "aba",
        "el_ella": "aba",
        "nosotros": "ábamos",
        "ustedes": "aban",
        "ellos": "aban",
    },
    "er": {
        "yo": "ía",
        "tu": "ías",
        "vos": "ías",
        "usted": "ía",
        "el_ella": "ía",
        "nosotros": "íamos",
        "ustedes": "ían",
        "ellos": "ían",
    },
    "ir": {
        "yo": "ía",
        "tu": "ías",
        "vos": "ías",
        "usted": "ía",
        "el_ella": "ía",
        "nosotros": "íamos",
        "ustedes": "ían",
        "ellos": "ían",
    },
}


PRETERITE_ENDINGS = {
    "ar": {
        "yo": "é",
        "tu": "aste",
        "vos": "aste",
        "usted": "ó",
        "el_ella": "ó",
        "nosotros": "amos",
        "ustedes": "aron",
        "ellos": "aron",
    },
    "er": {
        "yo": "í",
        "tu": "iste",
        "vos": "iste",
        "usted": "ió",
        "el_ella": "ió",
        "nosotros": "imos",
        "ustedes": "ieron",
        "ellos": "ieron",
    },
    "ir": {
        "yo": "í",
        "tu": "iste",
        "vos": "iste",
        "usted": "ió",
        "el_ella": "ió",
        "nosotros": "imos",
        "ustedes": "ieron",
        "ellos": "ieron",
    },
}


FUTURE_ENDINGS = {
    "yo": "é",
    "tu": "ás",
    "vos": "ás",
    "usted": "á",
    "el_ella": "á",
    "nosotros": "emos",
    "ustedes": "án",
    "ellos": "án",
}


CONDITIONAL_ENDINGS = {
    "yo": "ía",
    "tu": "ías",
    "vos": "ías",
    "usted": "ía",
    "el_ella": "ía",
    "nosotros": "íamos",
    "ustedes": "ían",
    "ellos": "ían",
}


def build_regular(verb, endings, use_infinitive=False):
    verb_type = get_verb_type(verb)
    stem = verb if use_infinitive else get_stem(verb)

    if verb_type is None:
        return None

    result = {}

    for pronoun in PRONOUNS:
        if use_infinitive:
            result[pronoun] = stem + endings[pronoun]
        else:
            result[pronoun] = stem + endings[verb_type][pronoun]

    return result


def conjugate(verb):
    verb = verb.lower().strip()

    result = {}

    if verb in IRREGULARS and "present" in IRREGULARS[verb]:
        result["present"] = IRREGULARS[verb]["present"]
    else:
        result["present"] = build_regular(verb, PRESENT_ENDINGS)

    result["imperfect"] = build_regular(verb, IMPERFECT_ENDINGS)
    result["preterite"] = build_regular(verb, PRETERITE_ENDINGS)
    result["future"] = build_regular(verb, FUTURE_ENDINGS, use_infinitive=True)
    result["conditional"] = build_regular(verb, CONDITIONAL_ENDINGS, use_infinitive=True)

    return result
