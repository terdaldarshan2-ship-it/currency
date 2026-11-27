from currency import usd_to_inr

def test_conversion():
    assert usd_to_inr(10) == 980

def test_zero():
    assert usd_to_inr(0) == 0