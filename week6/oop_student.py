import random

class Student:
    def __init__(self,ชื่อสกุล,ชื่อเล่น):
        self.name = ชื่อสกุล
        self.nickname = ชื่อเล่น
        self.score = random.randint(1,10) 
        self.editscore = random.randint(1,10)

    def scores(self):
        if self.score >= 5:
            print(f"ชื่อสกุล : {self.name}, ชื่อเล่น : {self.nickname}, คะแนน : {self.score} : คุณผ่าน")
        else :
            print(f"ชื่อสกุล : {self.name}, ชื่อเล่น : {self.nickname}, คะแนน : {self.score} : คุณตก")
             print("--------------------สอบแก้---------------------------")
        if self.editscore >= 5:
            print(f"ชื่อ-นามสกุล : {self.name} , ชื่อเล่น : {self.nikename}, คะแนน : {self.editscore } : คุณผ่าน")
        else :
            print(f"ชื่อ-นามสกุล : {self.name} , ชื่อเล่น : {self.nikename}, คะแนน : {self.editscore } : คุณตก")

Student1 = Student("หนึ่งธิดา อินทรชัย","สตางค์")
Student2 = Student("วิไลวรรณ พลเดช","พลอย")
Student3 = Student("วิลัยภรณ์ กัญจนกาญจน์","เป้")
Student4 = Student("รังสิมา พิเดช","วา")
Student5 = Student("ศศิวมล แซ่ด่าน","แบม")

Student1.scores()
Student2.scores()
Student3.scores()
Student4.scores()
Student5.scores()