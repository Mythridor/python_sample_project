from sample_project.main import (
    is_up,
    Status
)


def test_is_up():
    result = is_up()
    assert result == {"Status": Status.OK}
    assert result != {"Status": Status.NOK}
