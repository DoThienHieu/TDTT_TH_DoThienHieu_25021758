k=input().split()
a, b, c, d = map(int, k)
xx=True
for m in (a, b, c, d)
    if m > 1:
        for i in range(2, int(m**0.5)+1):
            if m % i == 0:
                xx=False
        if xx == True :
            print("có")
        else:
            print("không")
    else:
    print("không")