from app.services.log_processor import (
    categorize_log,
    detect_error_patterns
)



def test_categorize_error():

    result = categorize_log(
        "database error"
    )

    assert result == "ERROR"


def test_categorize_warning():

    result = categorize_log(
        "memory warning"
    )

    assert result == "WARNING"


def test_categorize_info():

    result = categorize_log(
        "user login successful"
    )

    assert result == "INFO"


def test_detect_timeout_pattern():

    result = detect_error_patterns(
        "server timeout occurred"
    )

    assert result == ["timeout"]


def test_detect_connection_refused_pattern():

    result = detect_error_patterns(
        "database connection refused"
    )

    assert result == ["connection refused"]


def test_detect_failed_pattern():

    result = detect_error_patterns(
        "request failed"
    )

    assert result == ["failed"]


def test_no_pattern_found():

    result = detect_error_patterns(
        "user login successful"
    )

    assert result is None



