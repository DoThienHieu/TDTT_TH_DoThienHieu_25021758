a, b = map(float, input("nhập 2 số a b: ").split())
if a == b == 0:
    print("vô số nghiệm")
elif a == 0 and b != 0:
    print("vô nghiệm")
else:
    print("nghiệm của phương trình ax + b = 0 là: {:.2f}".format(-b/a))