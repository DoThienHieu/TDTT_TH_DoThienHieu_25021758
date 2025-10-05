a, b, c = map(int, input("nhập 3 số nguyên dương a b c: ").split())
if a <= 0 or b <= 0 or c <= 0:
    print("No")
elif (a+b) >c and (a+c) > b and (b+c) > a:
    print("Yes")
else:
    print("No")
