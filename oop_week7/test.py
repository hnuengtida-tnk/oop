#ดักตัวอักษร ค่าติดลบ ค่า0 ในโค้ด หาพื้นที่ สี่เหลี่ยม สามเหลี่ยม วงกลม
while True:
    try:
        num = int(input('ใส่แม่สูตรคูณ '))
        if num == 0:
            raise ZeroDivisionError
        for i in range(1,13):
            print(f"{num} x {i} = {num+i} ")
    except ValueError:
        print('ใส่เฉพาะตัวเลข')
    except ZeroDivisionError:
        print('ห้ามหารด้วย 0')
    except :
        print('ผิดพลาดตรงไหนกัน')