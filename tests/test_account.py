from hypothesis import given
from hypothesis import strategies as s

from beancount_hypothesis import account


@given(
    s.tuples(
        s.integers(min_value=1, max_value=10),
        s.integers(min_value=1, max_value=10),
    )
)
def test_generate(mins: tuple[int, int]):
    gen = account.AccountGenerator(
        min_leaves=mins[0],
        max_leaves=mins[0] + 3,
        min_nodes=mins[1],
        max_nodes=mins[1] + 3,
    )

    roots = []
    for acct in gen.generate():
        roots.append(acct.split(":")[0])
        assert len(acct.split(":")) <= mins[0] + 3

    assert len(set(roots)) <= mins[1] + 3


def test_account_name():
    result = account.account_name().example()
    assert len(result.split(":")) == 3
