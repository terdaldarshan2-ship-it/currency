from currency import inr_to_usd

def test_conversion():
    assert round(inr_to_usd(980), 2) == 10.00


def test_zero():
    assert inr_to_usd(0) == 0