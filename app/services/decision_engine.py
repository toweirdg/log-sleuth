def decide_action(category, pattern):

    if category == "ERROR":
        return "Trigger alert + notify team"

    if pattern and "timout" in str(pattern):
        return "Restart service / check load"

    return "No action needed"
