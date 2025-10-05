a = int(input("số kwh điện tiêu thụ: "))
if 0 <= a <= 50:
    print("tiền điện:", a*1500)
elif 51 <= a <= 100:
    print("tiền điện:", 50*1500 + (a-50)*2000)
else:
    print("tiền điện:", 50*1500 + 50*2000 + (a-100)*3000 )
