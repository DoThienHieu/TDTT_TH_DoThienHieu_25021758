a, b, c = map(int, input("nhập 3 số nguyên dương a b c: ").split())
if a <= 0 or b <= 0 or c <= 0:
    print("không phải tam giác")
elif (a+b) >c and (a+c) > b and (b+c) > a:
    if a==b==c:
        print("tam giác đều")
    elif a==b or a==c or b==c:
        print("tam giác cân")
    else:
        print("tam giác thường")
else:
    print("không phải tam giác")
