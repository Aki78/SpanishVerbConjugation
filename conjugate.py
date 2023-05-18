from pattern.es import conjugate, INFINITIVE, PRESENT, PAST, FUTURE, CONDITIONAL, PRETERITE, \
    IMPERFECT, PRESENT_PERFECT, PAST_PERFECT, FUTURE_PERFECT, CONDITIONAL_PERFECT, \
    PRESENT_SUBJUNCTIVE
import json
import string

verbs = ["ser", "estar", "ir"]  # your list of verbs

# The subjects (singular and plural, 1st, 2nd, and 3rd person) for conjugation
subjects = [1, 2, 3]

tenses = {
    "Present": PRESENT,
    "Preterite": PRETERITE,
    "Imperfect": IMPERFECT,
    "Future": FUTURE,
    "Conditional": CONDITIONAL,
    "Present Perfect": PRESENT_PERFECT,
    "Past Perfect": PAST_PERFECT,
    "Future Perfect": FUTURE_PERFECT,
    "Conditional Perfect": CONDITIONAL_PERFECT,
    "Present Subjunctive": PRESENT_SUBJUNCTIVE
}

# Prepare the data
data = {letter: {} for letter in string.ascii_lowercase}
for verb in verbs:
    initial_letter = verb[0]
    if initial_letter not in data:
        data[initial_letter] = {}
    data[initial_letter][verb] = {}
    for tense_name, tense in tenses.items():
        data[initial_letter][verb][tense_name] = []
        for subject in subjects:
            data[initial_letter][verb][tense_name].append(conjugate(verb, tense, subject, sg = True))
            data[initial_letter][verb][tense_name].append(conjugate(verb, tense, subject, sg = False))

# Save to a JSON file
for initial_letter, verbs_data in data.items():
    if verbs_data:  # check if there is any verb for this initial letter
        with open(f"verbs_{initial_letter}.json", "w") as file:
            json.dump(verbs_data, file, ensure_ascii=False, indent=2)

