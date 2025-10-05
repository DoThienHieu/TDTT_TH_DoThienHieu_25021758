a = float(input("nhập số thực a:"))
nguyen = int(a) 
thap_phan = a - nguyen
if a < 0 and thap_phan <= -0.5:
    gan_nhat = nguyen - 1
elif thap_phan >= 0.5:
    gan_nhat = nguyen + 1
else:    
    gan_nhat = nguyen

if thap_phan == 0:
    len = nguyen
elif a > 0:
    len = nguyen + 1
else:
    len = nguyen

if thap_phan == 0:
    xuong = nguyen
elif a > 0:
    xuong = nguyen
else:
    xuong = nguyen - 1
print(len, xuong, gan_nhat)
