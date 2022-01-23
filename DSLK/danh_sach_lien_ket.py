from typing import List


class Nut:
    def __init__(self, gia_tri) -> None:
        self.gia_tri = gia_tri
        self.nut_ke_tiep = None
    #def
#class


class DSLienKet:
    def __init__(self) -> None:
        self.dau = None #tham chiếu đến nut đầu
        self.duoi = None #tham chiếu đến nut đuôi
    #def

    def in_ds(self):
        if self.dau == None:
            print("[]")
        
        hien_tai = self.dau
        stt = 0
        kq = 'DS['
        while hien_tai != None:
            stt +=1
            if stt == 1:
                kq += " " + str(hien_tai.gia_tri)
            else:
                kq += " -> " + str(hien_tai.gia_tri)
            hien_tai = hien_tai.nut_ke_tiep
        kq += " ]"

        print(kq)
    #def

    def them(self, gia_tri):
        nut = Nut(gia_tri)
        
        if self.dau == None:
            self.dau = nut
            self.duoi = nut
        else:
            self.duoi.nut_ke_tiep = nut
            self.duoi = nut
    #def

    def chen(self, vi_tri, gia_tri):
        nut = Nut(gia_tri)
        truoc = None# con trỏ trước
        hien_tai = self.dau # con tro duyet cac pt
        i = 0
        
        while i < vi_tri and hien_tai!=None:
            i += 1
            truoc = hien_tai
            hien_tai = hien_tai.nut_ke_tiep
        #while

        if truoc == None:
            # chen dau danh sach
            nut.nut_ke_tiep = self.dau
            self.dau = nut
            if self.duoi == None:
                self.duoi = nut
            #if
        else:
            if hien_tai == None:
                # them vao cuoi danh sach
                truoc.nut_ke_tiep = nut # tương đương self.duoi.nut_ke_tiep = nut
                self.duoi = nut
                return
            #if
            nut.nut_ke_tiep = truoc.nut_ke_tiep
            truoc.nut_ke_tiep = nut   
        #if-else
    #def

    def tim(self, gia_tri) -> List[int]:
        # danh sach rong
        if self.dau == None:
            return []
        l = []
        hien_tai = self.dau
        i = 0
        while hien_tai != None:
            if hien_tai.gia_tri == gia_tri:
                l.append(i)
            #if
            hien_tai = hien_tai.nut_ke_tiep
            i+=1
        #while
        return l
        
        # co nhieu hon 1 phan tui duoc tim thay
    #def

    def xoa(self, gt):
        hien_tai = self.dau
        truoc = None
        while hien_tai != None and hien_tai.gia_tri != gt:
            truoc = hien_tai
            hien_tai = hien_tai.nut_ke_tiep
        if hien_tai != None:
            # tim thay
            if hien_tai == self.dau  and hien_tai == self.duoi:
                # danh sach co duy nhat 1 phan tu
                self.dau = self.duoi = None
            elif hien_tai == self.dau:
                # xoa phan tu dau danh sach
                # self.dau = hien_tai
                self.dau = self.dau.nut_ke_tiep
            elif hien_tai == self.duoi:
                self.duoi = truoc
                self.duoi.nut_ke_tiep = None
            else:
                # xoa o giua "truoc va hien tai"
                truoc.nut_ke_tiep = hien_tai.nut_ke_tiep 
            
            del hien_tai
        #if
        #while
        # del hien_tai
    #def

    def cap_nhat(self, vi_tri, gia_tri):
        # 
        hien_tai = self.dau
        i = 0
        while i < vi_tri:
            i += 1
            hien_tai = hien_tai.nut_ke_tiep
        #while

        if hien_tai == None:
            return
        else:
            hien_tai.gia_tri = gia_tri
        #if-else
    #def

    def xoa_het(self):
        hien_tai = self.dau
        self.dau = self.duoi = None
        while hien_tai != None:
            tam = hien_tai
            hien_tai = hien_tai.nut_ke_tiep
            del tam
    #def
#class
