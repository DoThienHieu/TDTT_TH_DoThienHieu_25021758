a = int(input("nhập số nguyên n:"))
s = str(abs(a))[::-1]
if a < 0:
    print("-"+s)
else:
    print(s)