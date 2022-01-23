import random
from typing import List

from numpy import ma

def sinh_mang_ngau_nhien(num: int) -> List[int]:
    mang = []
    
    for i in range(num):
        mang.append(random.randint(0,100))

    return mang

def sap_xep_chen(mang: List[int]) -> None:
    n = len(mang)

    for i in range(n-1):
        vi_tri_min = i

        for j in range(i+1, n):
            if mang[vi_tri_min] > mang[j]:
                vi_tri_min = j

        mang[vi_tri_min], mang[i] = mang[i], mang[vi_tri_min]
        print(f"{i+1} - {mang}")

def main() -> None:
    mang = sinh_mang_ngau_nhien(10)
    print(f"Mang duoc sinh ngau nhien: {mang}")

    sap_xep_chen(mang)
    print(f"mang sau khi sap xep {mang}")

if __name__ == "__main__":
    main()

