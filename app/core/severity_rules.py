SEVERITY_RULES = {
    "timeout": {
        "severity": "HIGH",
        "action": "Check server load"
    },

    "connection refused": {
        "severity": "CRITICAL",
        "action": "Investigate service availability"
    },

    "failed": {
        "severity": "MEDIUM",
        "action": "Review application logs"
    }
}
