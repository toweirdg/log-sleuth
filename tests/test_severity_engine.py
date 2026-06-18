from app.services.severity_engine import get_severity


def test_severity_critical():

    result = get_severity(
        ["connection refused"]
    )

    assert result["severity"] == "CRITICAL"


def test_severity_high():

    result = get_severity(
        ["timeout"]
    )

    assert result["severity"] == "HIGH"


def test_severity_medium():

    result = get_severity(
        ["failed"]
    )

    assert result["severity"] == "MEDIUM"


def test_default_severity():

    result = get_severity(None)

    assert result["severity"] == "LOW"
