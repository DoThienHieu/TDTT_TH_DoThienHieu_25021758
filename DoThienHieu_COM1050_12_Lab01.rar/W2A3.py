a = int(input("Nhập sô nguyên a: "))
b = int(input("Nhập sô nguyên b: "))
tong = a + b
hieu = a - b
tich = a * b
phan_nguyen = a // b
phan_du = a % b
chia_thuc = a / b
print("Tổng:", tong)
print("Hiệu:", hieu)
print("Tích:", tich)
print("Chia lấy phần nguyên:", phan_nguyen)
print("Chia lấy phần dư", phan_du)
print("Chia thực lấy đến 2 chữ số thập phân: {:.2f}".format(chia_thuc) )