from app.core.severity_rules import SEVERITY_RULES


def get_severity(pattern):

    if not pattern:
        return {
            "severity": "LOW",
            "action": "No action needed"
        }

    for item in pattern:

        if item in SEVERITY_RULES:
            return SEVERITY_RULES[item]

    return {
        "severity": "LOW",
        "action": "No action needed"
    }
