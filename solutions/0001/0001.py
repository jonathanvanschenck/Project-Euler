"""


Created By: Jonathan D. B. Van Schenck



"""


# Sum of the multiples of 3 less than 1000
i = 999 // 3
sum = 3 * i * (i + 1) // 2


# Sum of the multiples of 5 less than 1000
i = 999 // 5
sum += 5 * i * (i + 1) // 2

# We double counted the multiples of 15, so remove one set

i = 999 // 15
sum -= 15 * i * (i + 1) // 2


print(sum)
