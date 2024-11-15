num = int (input('จำนวนคนที่จะป้อน : '))
for i in range(num):
    dic = {}
    print('กรุณากรอกข้อมูลคนที่'+str(i+1))
    dic['name'] = input("กรุณากรอกชื่อ : ")
    dic['nickname'] = input("กรุณากรอกชื่อเล่น : ")
    dic['stdid'] = input("กรุณากรอกรหัสประจำตัวนักศึกษา : ")
    dic['hobby'] = input("กรุณากรอกงานอดิเรก : ")
    dic['color'] = input("กรุณากรอกสีที่ชอบ : ")
    print('ข้อมูลคนที่'+str(i+1))
    print(dic)
