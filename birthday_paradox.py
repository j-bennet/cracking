import math

def birthdays(k):
    n = 365
    p_exist = 1. - (1. - 1. / n) ** k #1. - math.factorial(n) / math.factorial(n-k) / n ** k
    return p_exist

for i in range(10, 100, 10):
    print '%d: %.2f' % (i, 100 * birthdays(i))