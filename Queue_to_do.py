def solution(start, length):
    def xor(a, b):
        if(a % 2 == 0):
            rotation = [b, 1, b + 1, 0]
        else:
            rotation= [a, a^b, a - 1, (a - 1) ^b]
        return rotation[(b - a) % 4]
    
    c = 0
    for i in range(0, length):
        c ^= xor(start + (length * i), start + (length * i) + (length - i) -1)
    return c

#test
print(solution(17, 4))

