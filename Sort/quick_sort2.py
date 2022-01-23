import random
from typing import List

def sinh_mang_ngau_nhien(num: int)->List[int]:
    mang = []
    
    for i in range(num):
        mang.append(random.randint(0, 100))

    return mang

def quick_sort_2(mang: List[int]) -> List[int]:
    if len(mang) >1:
        lon_hon = []
        nho_hon = []
        bang    = []
        x = mang[0]
        
        for i in mang:
            if i > x:
                lon_hon.append(i)
            elif i == x:
                bang.append(i)
            else:
                nho_hon.append(i)

        return quick_sort_2(lon_hon) + bang + quick_sort_2(nho_hon)
    else:
        return mang

def main() -> None:
    mang = sinh_mang_ngau_nhien(10)
    print(f"mang sinh ngau nhien: {mang}")

    mang = quick_sort_2(mang)
    print("mang sau khi sap xep: ", mang)

if __name__ == "__main__":
    main()