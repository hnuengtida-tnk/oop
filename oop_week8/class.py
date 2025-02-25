class Student:
    def __init__(self,name,id,age,gradesM,gradesT,gradesE,gradesS,gradesSc):
        self.name = name
        self.id = id 
        self.age = age
        self.grades1 = gradesM
        self.grades2 = gradesT
        self.grades3 = gradesE
        self.grades4 = gradesS
        self.grades5 = gradesSc

    def average(self):
        grades = [self.grades1,self.grades2,self.grades3,self.grades4,self.grades5]
        gradesall = sum(grades) / len(grades)
        print(f"{self.name} | ได้เกรดเฉลี่ย : {gradesall:.2f}")

    def allresults(self):
        grades = [self.grades1,self.grades2,self.grades3,self.grades4,self.grades5]
        gradesall = sum(grades) / len(grades)
        print(f"ชื่อ : {self.name} หมายเลขประจำตัว : {self.id} อายุ : {self.age} เกรดเฉลี่ย : {gradesall:.2f} ")

mystudent1 = Student("นายเอ",100,20,2,4,3,1,4)
mystudent2 = Student("นายบี",101,19,3,1,3,4,4)

mystudent1.average()
mystudent2.average()
print('-------------------')
mystudent1.allresults()
mystudent2.allresults()