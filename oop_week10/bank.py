class Bank: #คลาสแม่แบบ
    def __init__(self,id,name,balance):
        self.id = id
        self.name = name
        self.__balance = balance
    def deposit(self,amount):
        if amount >= 100 :
            self.__balance += amount
        else :
            print('ยอดเงินไม่ถูกต้อง')
    def withdraw (self,amount): #ถอนเดงิน
        if amount >= 100 and amount <= self.balance :
            self.__balance -= amount
        else :
            print('ยอดเงินไม่ถูกต้อง')
    def showbalance(self): #เช็คยอด
        print(self.__balance)
        return self.__balance

id1 = Bank(1,"satang",2500)

id1.deposit(100)
print(f"คุณ {id1.name} มีเงิน = {id1.showbalance}")