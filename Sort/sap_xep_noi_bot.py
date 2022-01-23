import random as rd
from typing import List


def sinh_mang_ngau_nhien(num):
    mang = []

    for i in range(num):
        mang.append(rd.randint(-100, 100))

    return mang

def sap_xep_noi_bot(mang: List[int]) -> None:
    n = len(mang)
    
    for i in range(n-1):
        tiep_tuc = True
        
        for j in range(n-2, i-1, -1):
            if mang[j] > mang[j+1]:
                mang[j], mang[j+1] = mang[j+1], mang[j]
                tiep_tuc = True
        
        print(f"{i+1} - {mang}")
    
        if tiep_tuc == False:
            break

def main() -> None:
    x = int(input("nhap so phan tu mang sinh ngau nhien: "))
    mang = sinh_mang_ngau_nhien(x)
    print(mang)
    
    sap_xep_noi_bot(mang)
    print(f"Mang da sap xep noi bot {mang}")


if __name__ == "__main__":
    main()