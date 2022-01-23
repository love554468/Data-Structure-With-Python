import random as rd
def sinh_mang_tang_dan(num):
    so_dau_tien = rd.randint(-100,100)
    print(so_dau_tien)
    mang = [so_dau_tien]
    
    # print(tang)
    for i in range(1,num-1):
        tang = rd.randint(1,10)
        print(tang)
        print(mang[i-1])
        a= tang + mang[i-1]
        print(a)
        mang.append(a)
    return mang

print(sinh_mang_tang_dan(int(4)))