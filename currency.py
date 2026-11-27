from currency import inr_to_usd, usd_to_inr


def test_inr_to_usd():
    assert round(inr_to_usd(980), 2) == 10.00


def test_usd_to_inr():
    assert usd_to_inr(10) == 980


def test_zero():
    assert inr_to_usd(0) == 0
    assert usd_to_inr(0) == 0