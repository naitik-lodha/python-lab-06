from Interest import simple, compound

p = int(input("Enter principal: "))
r = int(input("Enter rate of interest: "))
t = int(input("Enter time in years: "))

print("Simple Interest: ", simple.Simple_Interest(p, r, t))
print("Compound Interest: ", compound.Compound_Interest(p, r, t))
