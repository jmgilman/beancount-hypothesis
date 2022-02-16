import string

from beancount_hypothesis import directive


def assert_account(account: str):
    assert len(account.split(":")) == 3


def assert_currency(currency: str):
    assert len(currency) == 3
    assert all([c in string.ascii_uppercase for c in currency])


def assert_filename(filename: str):
    assert len(filename.split("/")) > 1
    assert len(filename.split(".")[1]) == 3


def test_meta():
    result = directive.meta().example()
    assert isinstance(result["filename"], str)
    assert isinstance(result["lineno"], int)


def test_balance():
    result = directive.balance().example()
    assert_account(result.account)


def test_close():
    result = directive.balance().example()
    assert_account(result.account)


def test_commodity():
    result = directive.commodity().example()
    assert_currency(result.currency)

    result = directive.commodity(["USD", "CAD"]).example()
    assert result.currency in ["USD", "CAD"]


def test_custom():
    result = directive.custom().example()
    assert all([isinstance(v, str) for v in result.values])


def test_document():
    result = directive.document().example()
    assert_filename(result.filename)


def test_event():
    directive.event().example()


def test_note():
    result = directive.note().example()
    assert_account(result.account)


def test_open():
    result = directive.open().example()
    assert_account(result.account)
    [assert_currency(c) for c in result.currencies]


def test_pad():
    result = directive.pad().example()
    assert_account(result.account)
    assert_account(result.source_account)


def test_posting():
    directive.posting().example()


def test_price():
    result = directive.price().example()
    assert_currency(result.currency)

    result = directive.price(["USD", "CAD"]).example()
    assert result.currency in ["USD", "CAD"]


def test_transaction():
    result = directive.transaction().example()
    assert result.flag == "*"
    assert len(result.narration.split(" ")) > 1
    assert len(result.postings) <= 5
