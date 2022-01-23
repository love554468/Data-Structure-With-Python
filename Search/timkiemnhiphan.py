import random as rd

def sinh_mang_tang_dan(num):
    so_dau_tien = rd.randint(-100,100)

    mang = [so_dau_tien]
    
    # print(tang)
    for i in range(1,num-1):
        tang = rd.randint(1,10)
        a= tang + mang[i-1]
        # print(a)
        mang.append(a)
    return mang


def tim_kiem_nhi_phan(mang, x):
    left = 0
    right = len(mang) - 1

    while right >= left:
        print(f"{left} - {right}")
        mid = (right + left)//2
        if mang[mid] == x:
            return mid
        if mang[mid] > x:
            right = mid - 1
        else:
            left = mid + 1
        
    return -1

def main():
    mang = sinh_mang_tang_dan(20)
    print(mang)
    x = int(input("Nhap gia tri x can tim: "))

    idx = tim_kiem_nhi_phan(mang, x)
    if idx == -1:
        print(f"Khong tim thay {x}")
    else:
        print(f"x duoc tim thay tai vi tri {idx}")

if __name__ == "__main__":
    main()
        