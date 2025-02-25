class Cat:
    def __init__(self,ชื่อ,อายุ,สี,ความหิว):
        self.name = ชื่อ
        self.age = อายุ
        self.color = สี
        self.hnugry = ความหิว
    def eat(self,อาหาร):
        self.hnugry+=อาหาร

cat1=Cat(ชื่อ="ปลาทู",อายุ=11,สี="เทา",ความหิว=5)
cat2=Cat("ปลาลัง",10,"ส้ม",1)
