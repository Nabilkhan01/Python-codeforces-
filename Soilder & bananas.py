k, n, w = map(int, input().split())
cost = k * w*(w+1)/2
borrow = cost - n
if borrow > 0:
    print(borrow)
else:
    print('0')