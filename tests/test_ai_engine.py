from app.services.ai_engine import generate_insight


def test_error_with_pattern():

    result = generate_insight(
        "database timeout",
        "ERROR",
        ["timeout"]
    )

    assert "Issue detected" in result


def test_error_without_pattern():

    result = generate_insight(
        "unknown error",
        "ERROR",
        None
    )

    assert "investigation" in result.lower()


def test_warning_insight():

    result = generate_insight(
        "memory warning",
        "WARNING",
        None
    )

    assert "monitor" in result.lower()


def test_info_insight():

    result = generate_insight(
        "login successful",
        "INFO",
        None
    )

    assert "normally" in result.lower()
