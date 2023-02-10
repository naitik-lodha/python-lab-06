def Compound_Interest(p, r, t):
    amount = p * (pow((1 + r / 100), t))
    compound_interest = amount - p
    return compound_interest
