from typing import List
import random

def sinh_mang_ngau_nhien(num: int) -> List[int]:
    mang = []
    
    for i in range(num):
        mang.append(random.randint(0,100))

    return mang

def sap_xep_chen(mang: List[int])->None:
    n = len(mang)

    for j in range(1, n):
        bien_tam = mang[j]
        i= j

        while i >0 and bien_tam > mang[i-1]:
            mang[i] = mang[i-1]
            i = i-1
        mang[i] = bien_tam
        print(mang)

def main()-> None:
    mang = sinh_mang_ngau_nhien(10)
    print(f"sinh mang ngau nhien {mang}")

    sap_xep_chen(mang)
    print(f"Mang sau khi sap xep chen {mang}")


if __name__ == "__main__":
    main()