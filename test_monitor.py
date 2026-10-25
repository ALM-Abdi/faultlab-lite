from monitor import check_status
import pytest

def test_success_status():
    assert check_status(200) is True
    assert check_status(201) is True


def test_error_status():
    assert check_status(404) is False
    assert check_status(500) is False

@pytest.mark.parametrize("status_code, expected", [
    (199, False),
    (200, True),
    (299, True),
    (300, False)
])
def test_boundary_status(status_code, expected):
    assert check_status(status_code) is expected