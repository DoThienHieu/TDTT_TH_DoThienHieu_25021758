a = int(input("Nhập 1 số bất kì từ 0 đến 9: "))
match a:
    case 0:
        print("không")
    case 1:
        print("một")
    case 2:
        print("hai")
    case 3:
        print("ba")
    case 4:
        print("bốn")
    case 5:
        print("năm")
    case 6:
        print("sáu")
    case 7:
        print("bảy")
    case 8:
        print("tám")
    case 9:
        print("chín")
    case _:
        print("số không hợp lệ")