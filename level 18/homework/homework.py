m = 10
o = "mate"

for i in range(m):
    print(o)


for i in range(1,21):
    print(i)


for i in range(20,-1,-1):
    print(i)


w = 0

for i in range(1,51):
    w += 1
    print(w)


even_sum = 0

for i in range(1, 11):
    if i % 2 == 0:
        even_sum += i

print("ლუწი რიცხვების ჯამი:", even_sum)



number = int(input("შეიყვანეთ რიცხვი: "))

for i in range(0, number + 1):
    if i % 2 == 0:
        print(f"{i} is Even")
    else:
        print(f"{i} is Odd")
