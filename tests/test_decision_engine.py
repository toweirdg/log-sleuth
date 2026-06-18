from app.services.decision_engine import decide_action


def test_error_action():

    result = decide_action(
        "ERROR",
        None
    )

    assert result == "Trigger alert + notify team"


def test_default_action():

    result = decide_action(
        "INFO",
        None
    )

    assert result == "No action needed"


def test_timeout_action():

    result = decide_action(
        "INFO",
        ["timeout"]
    )

    assert result == "Restart service / check load"
