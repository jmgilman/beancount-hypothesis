from beancount.core import position

from beancount_hypothesis import data


def test_decimal():
    result = data.decimal().example()
    assert result is not None
    assert result == result  # Fails if NaN
    assert result >= 1 and result <= 101


def test_amount():
    result = data.amount().example()
    assert result.currency == "USD"

    result = data.amount(["USD", "CAD"]).example()
    assert result.currency in ["USD", "CAD"]


def test_cost():
    result = data.cost().example()
    assert result.currency == "USD"

    result = data.cost(["USD", "CAD"]).example()
    assert result.currency in ["USD", "CAD"]


def test_costspec():
    result = data.costspec().example()
    assert result.currency == "USD"

    result = data.costspec(["USD", "CAD"]).example()
    assert result.currency in ["USD", "CAD"]


def test_inventory():
    result = data.inventory().example()
    assert all([isinstance(p, position.Position) for p in result])
    assert len(result) <= 3


def test_position():
    data.position().example()
