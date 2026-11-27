def inr_to_usd(inr):
    return inr / 98


if __name__ == "__main__":
    amount = float(input("Enter INR: "))
    print("USD:", round(inr_to_usd(amount), 2))