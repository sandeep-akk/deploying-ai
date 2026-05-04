def tool_service(query):
    q = query.lower()

    # simple calculator
    if any(op in q for op in ["+", "-", "*", "/"]):
        try:
            return str(eval(query))
        except:
            return "Invalid math expression"

    # simple fallback tool
    if "time" in q:
        return "I cannot access real-time clock yet."

    return "No tool matched your request."