# Test 1
# By use of a function that accepts parameters, calculate the simple interest given principal as 45000, rate is 7% and the time taken is 8 years. (si = p*r*t/100)

def simpleInterest(p, r, t):
    SI = (p * r * t / 100)
    print("This is the simple interest: ", SI)

simpleInterest(45000, 7 , 8)


# Use the same function inside of a loop to calculate two other simple interests. Note use your own principal, rate and time.

simpleInterest(24000, 15, 10)
simpleInterest(300000, 20, 5)