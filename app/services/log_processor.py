import re
from collections import Counter

global_log_memory = []


def categorize_log(message: str):
    message = message.lower()

    if "error" in message:
        return "ERROR"
    elif "warning" in message:
        return "WARNING"
    else:
        return "INFO"


def detect_repeated_patterns(message: str):
    global_log_memory.append(message)
    counts = Counter(global_log_memory)

    if counts[message] > 3:
        return True

    return False


def detect_error_patterns(message: str):
    patterns = [r"timeout", r"connection refused", r"failed", r"exception"]

    found_patterns = []

    for pattern in patterns:
        if re.search(pattern, message.lower()):
            found_patterns.append(pattern)

    return found_patterns if found_patterns else None
