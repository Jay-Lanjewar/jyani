questions = [
    {
        "id": "q1",
        "text": "How's your energy right now?",
        "options": [
            {"label": "Completely drained", "energy": -2, "valence": 0, "social": 0},
            {"label": "Low, sluggish", "energy": -1, "valence": 0, "social": 0},
            {"label": "Neutral, just okay", "energy": 0, "valence": 0, "social": 0},
            {"label": "Fairly energetic", "energy": 1, "valence": 0, "social": 0},
            {"label": "Buzzing, ready to go", "energy": 2, "valence": 0, "social": 0},
        ],
    },
    {
        "id": "q2",
        "text": "What's your emotional state closest to?",
        "options": [
            {"label": "Sad or hurt", "energy": 0, "valence": -2, "social": 0},
            {"label": "Anxious or tense", "energy": 0, "valence": -1, "social": 0},
            {"label": "Blank, nothing much", "energy": 0, "valence": 0, "social": 0},
            {"label": "Content, at ease", "energy": 0, "valence": 1, "social": 0},
            {"label": "Happy, on top", "energy": 0, "valence": 2, "social": 0},
        ],
    },
    {
        "id": "q3",
        "text": "Do you want to feel connected or be in your own world?",
        "options": [
            {"label": "Deep in my own world", "energy": 0, "valence": 0, "social": -2},
            {"label": "Mostly alone", "energy": 0, "valence": 0, "social": -1},
            {"label": "Somewhere in between", "energy": 0, "valence": 0, "social": 0},
            {"label": "Around people", "energy": 0, "valence": 0, "social": 1},
            {"label": "Full social mode", "energy": 0, "valence": 0, "social": 2},
        ],
    },
    {
        "id": "q4",
        "text": "Pick the weather that matches your mood:",
        "options": [
            {"label": "Heavy rain at night", "energy": -1, "valence": -1, "social": -1},
            {"label": "Overcast, grey sky", "energy": -1, "valence": -1, "social": 0},
            {"label": "Mild, breezy afternoon", "energy": 0, "valence": 1, "social": 0},
            {"label": "Golden hour sunset", "energy": 1, "valence": 1, "social": 1},
            {"label": "Bright, blazing noon", "energy": 2, "valence": 1, "social": 1},
        ],
    },
    {
        "id": "q5",
        "text": "What do you feel like doing right now?",
        "options": [
            {"label": "Just lie down and zone out", "energy": -2, "valence": 0, "social": -1},
            {"label": "Think quietly alone", "energy": -1, "valence": 0, "social": -2},
            {"label": "Watch something or read", "energy": 0, "valence": 0, "social": 0},
            {"label": "Go for a walk or light work", "energy": 1, "valence": 1, "social": 0},
            {"label": "Dance, run, do something intense", "energy": 2, "valence": 1, "social": 1},
        ],
    },
    {
        "id": "q6",
        "text": "How do you want to feel AFTER listening?",
        "options": [
            {"label": "Understood, less alone", "energy": 0, "valence": 1, "social": -1},
            {"label": "Calm and grounded", "energy": -1, "valence": 1, "social": 0},
            {"label": "Focused and sharp", "energy": 1, "valence": 0, "social": -1},
            {"label": "Uplifted and lighter", "energy": 1, "valence": 2, "social": 0},
            {"label": "Fired up and unstoppable", "energy": 2, "valence": 1, "social": 1},
        ],
    },
    {
        "id": "q7",
        "text": "What's the last thing that happened to you?",
        "options": [
            {"label": "Something disappointing", "energy": -1, "valence": -2, "social": -1},
            {"label": "A stressful moment", "energy": 1, "valence": -1, "social": 0},
            {"label": "Nothing specific, just existing", "energy": 0, "valence": 0, "social": 0},
            {"label": "Something good, small win", "energy": 1, "valence": 1, "social": 0},
            {"label": "Something exciting or big", "energy": 2, "valence": 2, "social": 1},
        ],
    },
    {
        "id": "q8",
        "text": "If your mood were a colour right now, it'd be:",
        "options": [
            {"label": "Deep grey or black", "energy": -1, "valence": -2, "social": -1},
            {"label": "Muted blue or purple", "energy": -1, "valence": -1, "social": 0},
            {"label": "Soft beige or cream", "energy": 0, "valence": 0, "social": 0},
            {"label": "Warm orange or amber", "energy": 1, "valence": 1, "social": 1},
            {"label": "Electric yellow or red", "energy": 2, "valence": 1, "social": 1},
        ],
    },
    {
        "id": "q9",
        "text": "What kind of songs do you prefer?",
        "options": [
            {"label": "Songs I already know and love", "pref": "familiar"},
            {"label": "Mix of known and new", "pref": "mixed"},
            {"label": "Discover new songs", "pref": "new"},
        ],
    },
    {
        "id": "q10",
        "text": "What kind of music era do you lean towards?",
        "options": [
            {"label": "Old classics (60s–90s)", "era": "old"},
            {"label": "2000s–2010s", "era": "mid"},
            {"label": "Modern songs", "era": "modern"},
            {"label": "Depends on mood", "era": "dynamic"},
        ],
    },
    {
        "id": "q11",
        "text": "Which languages do you prefer?",
        "options": [
            {"label": "Hindi", "lang": "hindi"},
            {"label": "Marathi", "lang": "marathi"},
            {"label": "English", "lang": "english"},
            {"label": "Mix of all", "lang": "mixed"},
        ],
    },
]


def calculate_scores(answers: dict) -> tuple:
    energy, valence, social = 0, 0, 0
    for q_id, option_index in answers.items():
        q = next(q for q in questions if q["id"] == q_id)
        option = q["options"][option_index]
        energy += option.get("energy", 0)
        valence += option.get("valence", 0)
        social += option.get("social", 0)
    return energy, valence, social


def build_answer_summary(answers: dict) -> str:
    lines = []
    for q_id, option_index in answers.items():
        q = next(q for q in questions if q["id"] == q_id)
        chosen = q["options"][option_index]["label"]
        lines.append(f'- {q["text"]} -> "{chosen}"')
    return "\n".join(lines)
