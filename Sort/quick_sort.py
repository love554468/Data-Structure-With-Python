# điểm yếu là nó vô tình sort rồi thì cho máy nó vẫn chạy

from multiprocessing import managers
from typing import List

import random


def sinh_mang_ngau_nhien(num: int) -> List[int]:
    mang = []

    for i in range(num):
        mang.append(random.randint(0, 100))

    return mang

def phan_vung_tu_dong(mang: List[int], duoi, tren) -> int:
    # chia mang thanh 2 phan boi quan chot(pivot)
    # mot mang nho hon chot nam ben trai
    # mot mang lon hon chot nam ben phai
    i = duoi - 1
    chot = mang[tren]

    for j in range(duoi, tren):
        if mang[j] > chot:
            i = i + 1
            mang[i], mang[j] = mang[j], mang[i]
    
    mang[i+1], mang[tren] = mang[tren], mang[i+1]

    return i+1

def quick_sort(mang: list[int], tren: int, duoi: int):
    if tren>duoi:
        vitri = phan_vung_tu_dong(mang, tren, duoi)
        phan_vung_tu_dong(mang, duoi, vitri -1)
        phan_vung_tu_dong(mang, vitri+1, tren)

def main():
    mang = sinh_mang_ngau_nhien(10)
    print("mang da sinh: ", mang)

    quick_sort(mang, 0, len(mang) -1)
    print(mang)

if __name__ == "__main__":
    main()