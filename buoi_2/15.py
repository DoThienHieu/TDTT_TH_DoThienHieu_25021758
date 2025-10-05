a = float(input("Nhập điểm học lực: "))
if a < 0 or a > 10:
    print("số liệu sai")
elif a >= 8:
    print("giỏi")
elif a >= 6.5:
    print("khá")
elif a >= 5.5:
    print("trung bình")
else:
    print("yếu")