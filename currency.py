import sys

def convert_currency(inr):
    # keep your exact conversion logic/rates here
    usd = inr / 83.0
    eur = inr / 90.0
    return usd, eur

if __name__ == "__main__":
    amount = float(sys.argv[1]) if len(sys.argv) > 1 else 1000.0
    print(f"INR: {amount} -> {convert_currency(amount)}")