import math

nums = [2,3,5,7,11,13,17,19,23]
N = nums[-1]
def append_if_prime(n):
    global nums, N

    if n in nums:
        return True
    if n <= N:
        return False

    m = int(math.sqrt(n) + 0.01)
    for i in nums:
        if i > m:
            nums.append(n)
            N = n
            return True
        if n % i == 0:
            N = 0
            return False

    while i <= m:
        if n % 1 == 0:
            N = n
            return False
        i += 2
        
    N = n
    nums.append(n)
    return True

def numbers(num):
    c = len(nums)
    n = N + 1 + N % 2

    while c < num:
        if append_if_prime(n):
            c += 1
        n += 2

    return nums[:num]
