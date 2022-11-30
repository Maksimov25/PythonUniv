b1 = 1
b2 = 1
n = input()
n = int(n)
i = 0
while i < n - 2:
    b_sum = b1 + b2
    b1 = b2
    b2 = b_sum
    i = i + 1
print(b2)
