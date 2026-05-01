def generate_insight(message: str, category: str, pattern):
	
	if category == "ERROR":
		if pattern:
			return f"Issue detected: {pattern}. Likely system instability."
		return "General error detected. Needs investigation."

	if category == "WARNING":
		return "Warning detected. Monitor system closely."

	return "System operating normally."
