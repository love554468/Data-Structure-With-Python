from typing import List


import random as rd

def sinh_mang(num: int):
    mang = []
    for i in range(num):
        mang.append(rd.randint(-100, 100))
    return mang

def tim_tuyen_tinh(mang, x):
    l = len(mang)
    for i in range(l):
        if mang[i] == x:
            return i
    return -1


def main():
    mang = sinh_mang(20)
    print(mang)

    x = int(input("Nhap so can tim kiem: "))
    idx = tim_tuyen_tinh(mang, x)

    if idx == -1:
        print(f"Khong tim thay {x} trong mang")
    else:
        print(f"{x} duoc tim thay tai vi tri {idx} cua mang")


if __name__ == "__main__":
    main()