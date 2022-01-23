from danh_sach_lien_ket import *

def main():
    ds = DSLienKet()
    ds.in_ds()

    # a - them
    print("Them-------------------")
    ds.them("10")
    ds.in_ds()

    ds.them("20")
    ds.in_ds()
    # b - chen
    print("Chen -----------------")
    gt = 4
    vt = 1
    print(f"chen gia tri {gt} tai vi tri {vt}")
    ds.chen(vt, gt)
    ds.in_ds()

    gt = 21
    vt = 3
    print(f"chen gia tri {gt} tai vi tri {vt}")
    ds.chen(vt, gt)
    ds.in_ds()
    
    gt = 5
    vt = 0
    print(f"chen gia tri {gt} tai vi tri {vt}")
    ds.chen(vt, gt)
    ds.in_ds()

    gt = 5
    vt = 0
    print(f"chen gia tri {gt} tai vi tri {vt}")
    ds.chen(vt, gt)
    ds.in_ds()

    # f - tim
    print("tim ---------------------------")
    gt = 3
    print(f"tim gia tri {gt} trong linklist")
    re = ds.tim(gt)
    print(f"list vi tri tim thay co gia tri tuong duong la {re}") if len(re) else print("Khong co gia tri nao duoc tim thay tuong duong")


    gt = 5
    print(f"tim gia tri {gt} trong linklist")
    re = ds.tim(gt)
    print(f"list vi tri tim thay co gia tri tuong duong la {re}") if len(re) else print("Khong co gia tri nao duoc tim thay tuong duong")

    # e - xoa
    print("xoa ---------------------------")
    gt = 3
    print(f"xoa gia tri {gt} trong ds")
    ds.xoa(gt)
    ds.in_ds()

    gt = 5
    print(f"xoa gia tri {gt} trong ds")
    ds.xoa(gt)
    ds.in_ds()

    gt = 10
    print(f"xoa gia tri {gt} trong ds")
    ds.xoa(gt)
    ds.in_ds()
    #failed

    # d - cap nhat
    print("Cap nhat -------------------")
    vt = 1
    gt = 100
    ds.cap_nhat(vt, gt)
    print(f"cap nhat tai vi tri {vt} gia tri {gt}")
    ds.in_ds()

    vt = 2
    gt = 12233
    ds.cap_nhat(vt, gt)
    print(f"cap nhat tai vi tri {vt} gia tri {gt}")
    ds.in_ds()

    vt = 4
    gt = 1111
    ds.cap_nhat(vt, gt)
    print(f"cap nhat tai vi tri {vt} gia tri {gt}")
    ds.in_ds()
    
    # c - xoa het
    print(" Xoa het =------------------")
    ds.xoa_het()
    ds.in_ds()

#def

if __name__ == "__main__":
    main()
#if
