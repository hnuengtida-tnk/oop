import random
print('โปรแกรมเป่ายิงฉุบ')
while True:
    a = random.choice(["ค้อน","กรรไกร","กระดาษ"])
    print(a)
    print('เลือก ค้อน กระดาษ กรรไกร')
    i = str(input("คุณเลือก : "))
    if i == a :
        print("ผลลัพธ์คือ เสมอกัน")
        print('------------------')
    elif a == "กรรไกร" and i == "ค้อน" :
        print("ผลลัพธ์คือ คุณชนะค่ะ")
        print('------------------')
    elif a == "ค้อน"and i == "กระดาษ" :
        print("ผลลัพธ์คือ คุณชนะค่ะ")
        print('------------------')
    elif a == "กระดาษ"and i == "กรรไกร" :
<<<<<<< HEAD
        print("ผลลัพธ์คือ คุณชนะค่ะ")
        print('------------------')
    elif a == "กระดาษ"and i == "กรรไกร" :
=======
>>>>>>> cd7922e963991b7c4bf22ca0678ee65369bcacf3
        print("ผลลัพธ์คือ คุณแพ้ค่ะ")
        print('------------------')