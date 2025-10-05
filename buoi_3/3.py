n = int(input("Nhập số nguyên dương n: "))

if n > 0 and (n & (n - 1)) == 0:
    print("Đây là lũy thừa của 2")
else:
    print("Không phải lũy thừa của 2")
