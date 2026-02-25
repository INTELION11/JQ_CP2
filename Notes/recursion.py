number = 5
factorial = 1
while number > 0:
    factorial *= number
    number -= 1
print(factorial)


def factor(num):
    if num == 1: return 1
    # ^^^^^ Base Case , The point when we stopp calling ourselvs
    return num * factor(num-1)
#while True:
    max = print(factor(997)*factor(700))
    max = max + max; print(max)
# notes
number = 10
sequence = [1,1]
for i in range(1,number-1):
    sequence.append(sequence[i] + sequence[i-1])
print(sequence)

recursive_sequence = [1,1]
"""def fibanachi(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        recursive_sequence.append(recursive_sequence[fibanachi(n )])"""
def fibanachi(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibanachi(n-1) + fibanachi(n-2)
print(fibanachi(10))

import hashlib as fibana

# save password hashed, when they type it again use the same seed and check if the hashes are the same, make the seed be like the first three letters of the user name to save the seed

alr = "what"
#gshsj