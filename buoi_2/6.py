s = input("nhập 3 cạnh của tam giác: ").split()
a, b, c = map(int, s)
p = (a+b+c)/2
if (a+b) >c and (a+c) > b and (b+c) > a:
    print("diện tích tam giác là: {:.1f}".format((p *(p-a)*(p-b)*(p-c))**0.5))
else:
    print("không phải tam giác")

          