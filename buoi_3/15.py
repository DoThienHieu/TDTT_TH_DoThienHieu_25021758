scores = float(input("nhập điểm trung bình: "))
if scores < 0:
    print("sai số liệu")
elif scores >= 8:
    print("giỏi")
elif scores >= 6.5:
    print("khá")
elif scores >= 5.0:
    print("trung bình")
else:
    print("yếu")