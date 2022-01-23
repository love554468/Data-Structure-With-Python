
class NganXep:
    def __init__(self) -> None:
        self.danh_sach = []
    #def

    def la_rong(self):
        # is_empty()
        return len(self.danh_sach) == 0
    #def

    def __str__(self):
        #in ra danh sach cac pt ngan xep
        if len(self.danh_sach) == 0:
            return ""

        if len(self.danh_sach) == 1:
            return self.danh_sach

        s = " -> ".join([str(i) for i in self.danh_sach[1:]])
        return "Danh sach: [ " + str(self.danh_sach[0]) +" -> " + s + " ]."
    #def

    def day_vao(self, x):
        #push
        self.danh_sach.insert(0, x)
    #def
    
    def lay_ra(self):
        #pop
        if self.la_rong():
            return None

        return self.danh_sach.pop(0)
    #def

#class

if __name__ == "__main__":
    ds_a = NganXep()
    print(ds_a)
    for i in range(1,6):
        print(f"them vao {i}")
        ds_a.day_vao(i)
        # print(ds_a)
    print(ds_a)
    for i in range(1,6):
        print(f"Lay ra {i}")
        print(ds_a.lay_ra())
        # print(ds_a)