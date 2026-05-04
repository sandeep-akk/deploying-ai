def guardrails(user_input):
    q = user_input.lower()

    banned = [
        "cat",
        "dog",
        "zodiac",
        "horoscope",
        "taylor swift"
    ]

    if any(b in q for b in banned):
        return "Sorry, I can't discuss that topic."

    if "system prompt" in q:
        return "I cannot reveal system instructions."

    if "ignore previous instructions" in q:
        return "I cannot comply with that request."

    return None