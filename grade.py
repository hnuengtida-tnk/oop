print ('โปรแกรมคำนวณเกรด')
a = int(input('กรุณาใส่คะเเนน'))
if a < 0 or a > 100 :
    print('กรุณากรอก0 - 100 ')
elif a >= 80:
    print('คุณได้เกรด 4')
elif a >= 70:
    print('คุณได้เกรด 3')
elif a >= 60:
    print('คุณได้เกรด 2')
elif a >= 50:
    print('คุณได้เกรด 1')
else :
    print('คุณสอบตก')
    print('เราจะให้โอกาสคุณแก้ หากเลือก 1 ถ้าไม่ต้องการแก้โปรดเลือก 2')
    c = int(input('เลือก : '))
    if c == 1:
        d = 50 - a
        print(f'คุณขาดคะเเนน{d}')
    elif c == 2:
        print('คุณสอบตก')
    else :
        print('กรุณาเลือก 1 หรือ 2 ')