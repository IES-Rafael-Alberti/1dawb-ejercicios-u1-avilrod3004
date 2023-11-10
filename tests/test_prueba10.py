import pytest
from prueba10 import mayor

@pytest.mark.parametrize(
    "input_x, input_y, expected",
    [
        (10, 10, 0),
        (3, 10, 10),
        (5, 1, 5)
    ]
)

def test_mayor_params(input_x, input_y, expected):
    assert mayor(input_x, input_y) == expected