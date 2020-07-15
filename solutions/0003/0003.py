"""


Created By: Jonathan D. B. Van Schenck

Method:


"""

# Initialize the dividend
dividend = 600851475143#13195

# Initialize trial prime factor
factor = 2

# Initialize list of prime factors
factors = []

# Loop until everything is divided out
while dividend > 1:
    # Test if the trial factor divides the dividend
    #  Note: by construction, no composite factor will ever pass this test
    remainder = dividend % factor
    if remainder == 0:
        # If so, append the factor
        factors.append(factor)
        dividend = dividend // factor
    else:
        # Else move on
        factor += 1

print(factors[-1])
