a = 0 
while True:
    i = int(input("ใส่ค่า: "))
    if i > 0 :
        a += i
        print(f'ผลรวมตอนนี้ {a}')
    elif i == 0 :
        print(f'ผลรวมตอนนี้ {a}')
        print(f'ผลรวมทั้งหมด {a}')
        break
