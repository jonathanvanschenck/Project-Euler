"""


Created By: Jonathan D. B. Van Schenck

Method:
The sum of two numbers with the same parity is even and the sum of
two number with opposite parity is odd, so the Fib. numbers will have the pattern:

odd, odd, even, odd, odd, even, odd, odd, even, ...

So, we don't need to check the parity, we can just loop through and accumulate
every third Fib number

"""
# Initialize the Fib. Sequence
sum = 0
old_value = 1
new_value = 2

# Loop until we hit 4 million
while new_value < 4000000:
    # Accumulate the even value
    sum += 1*new_value
    # Find the next three Fib numbers
    for _ in range(3):
        temp = new_value + old_value
        old_value = 1*new_value
        new_value = 1*temp

print(sum)
