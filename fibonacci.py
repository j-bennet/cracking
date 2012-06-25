def fact(n):
    print 'n =', n
    if n == 0:
        return 1
    return n * fact(n - 1)

def rabbits(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n >= 2 and n <= 5:
        return rabbits(n - 1) + rabbits(n - 2)
    return rabbits(n - 1) + rabbits(n - 2) - rabbits(n - 5)

def fast_rabbits(n):
    current = 0
    after = 1
    dead = []
    for i in range(0, n):
        
        dead.append(current)
        if len(dead) > 4: dead.pop(0)

        if len(dead) < 4:
            current, after = after, current + after
        else:
            current, after = after, current + after - dead[0]
    return current

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def fast_fibonacci(n):
    current = 0
    after = 1
    for i in range(0, n):
        current, after = after, current + after
    return current

fact(6)

#print fibonacci(0)
#print fibonacci(5)
#print fibonacci(8)
#print fibonacci(24)
#print fibonacci(36)

#print fast_fibonacci(6)
#print fast_fibonacci(20)
#print fast_fibonacci(8)
#print fast_fibonacci(24)
#print fast_fibonacci(36)

#print rabbits(10)
#print rabbits(15)
#print rabbits(20)

#print fast_rabbits(10)
#print fast_rabbits(15)
#print fast_rabbits(20)
