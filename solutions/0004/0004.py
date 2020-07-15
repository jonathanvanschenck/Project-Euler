"""


Created By: Jonathan D. B. Van Schenck

Method:


"""

# 
# ones_place = {digit:[] for digit in range(10)}
# tens_place = {digit:[] for digit in range(10)}
#
# for d1 in range(10):
#     for d2 in range(10):
#         product = d1 * d2
#         ones_place[product % 10].append([d1,d2])
#         tens_place[product // 10].append([d1,d2])
#
# for digit in range(1,9):
#     ones_list = ones_place[digit]
#     tens_list = tens_place[digit]
#     for b,d in ones_list:
#         for a,c in tens_list:
#             if (a*d + c*b + b*d//10 - a*c - a*d//10 - c*b//10) % 10 == 0:
#                 print(a,b,c,d,(10*a+b)*(10*c+d))
