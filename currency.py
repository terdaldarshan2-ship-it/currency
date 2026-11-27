def usd_to_inr(usd):     
    return usd * 98


if __name__ == "__main__":
    amount = float(input("Enter INR: "))
    print("USD:", round(inr_to_usd(amount), 2))