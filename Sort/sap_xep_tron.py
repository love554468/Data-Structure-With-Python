def sap_xep_tron(mang):
    n = len(mang)
    
    if n>1:
        giua = n//2
        mang_trai = mang[:giua]
        mang_phai = mang[giua:]

        sap_xep_tron(mang_trai)
        sap_xep_tron(mang_phai)

        i = j = k = 0
        while i< len(mang_trai) and j < len(mang_phai):
            if mang_trai[i] < mang_phai[j]:
                mang[k] = mang_trai[i]
                i = i + 1
            else:
                mang[k] = mang_phai[j]
                j = j + 1

            k = k + 1

        while i < len(mang_trai):
            mang[k] = mang_trai[i]
            i +=1
            k +=1

        while j < len(mang_phai):
            mang[k] = mang_phai[j]
            j +=1
            k +=1

 
        