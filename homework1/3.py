a = input("Nhập chữ cái:")
t = ord(a)
if 97 <=t <=122:
    print(chr(t -32))
else:
    print(chr(t +32))