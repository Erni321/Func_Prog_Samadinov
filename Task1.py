def climbStairs(n):
    if n <= 2:
        return n

    step1, step2 = 2, 1

    for i in range(3, n + 1):
        current = step1 + step2
        step2 = step1
        step1 = current

    return step1
print(climbStairs(2))  #  2
print(climbStairs(4))  #  5
print(climbStairs(5))  #  8