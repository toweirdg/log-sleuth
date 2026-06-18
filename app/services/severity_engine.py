from app.core.severity_rules import SEVERITY_RULES


def get_severity(patterns):

    if not patterns:
        return {
            "severity": "LOW",
            "action": "No action needed"
        }

    highest_priority = {
        "LOW": 1,
        "MEDIUM": 2,
        "HIGH": 3,
        "CRITICAL": 4
    }

    selected_rule = {
        "severity": "LOW",
        "action": "No action needed"
    }

    for pattern in patterns:

        if pattern in SEVERITY_RULES:

            rule = SEVERITY_RULES[pattern]

            if (
                highest_priority[rule["severity"]]
                >
                highest_priority[selected_rule["severity"]]
            ):
                selected_rule = rule

    return selected_rule
