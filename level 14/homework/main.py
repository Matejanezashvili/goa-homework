# iteration ნიშნავს პროცესის განმეორებას.
# sequecing ნიშნავს რომ მოქმედებები უნდა შესრულდეს აუცილებლად თანმიმდევრობით.
# selection ნიშნავს როცა არჩევანს ვაკეთებთ რაღაცის შესრულებას შორის, მხოლოდ თუ პირობები შესრულებულია.












x = 5
y = 5
print(x == y)  # True

x = 10
y = 15
print(x != y)  # True


x = 4
y = 8
print(x < y)  # True


x = 7
y = 3
print(x > y)  # True

x = 6
y = 6
print(x <= y)  # True


x = 9
y = 5
print(x >= y)  # True


x = 10
y = 5
z = 15
print(x > y and z > y)  # True

x = 10
y = 5
z = 3
print(x > y or z > y)  # True



x = 20
y = 10
z = 15
print(x > y and x > z)  # True










name = input("შეიყვანეთ თქვენი სახელი: ")
age = int(input("შეიყვანეთ თქვენი ასაკი: "))
height = float(input("შეიყვანეთ თქვენი სიმაღლე: "))
if age>18 and name == "მათე" and height> 1.80:
    print("მონაცემები სწორია")
else:
    print("მონაცემები არასწორია")






# flouchart












name = "mate"

if name:
    print("მე მქვია მათე")
else:
    print("ეს არ არის ჩემი სახელი")






password = "1234"

if password == "1234":
    print("შედეგიანი ავტორიზაცია!")
else:
    print("არასწორი მომხმარებელი ან პაროლი!")


















score = 85

if score >= 90 and score <= 100:
    print("შენი ნიშანი A!")
elif score >= 80 and score < 90:
    print("შენი ნიშანი B!")
elif score >= 70 and score < 80:
    print("შენი ნიშანი C!")
else:
    print("შენი ნიშანი D ან F!")







age = 16
parent_permission = True

if age >= 18 or parent_permission:
    print("თქვენ შეგიძლიათ ფილმის ყურება!")
else:
    print("თქვენ არ შეგიძლიათ ფილმის ყურება!")








age = 20
high_school_diploma = True

if age >= 18 and high_school_diploma:
    print("თქვენ შეგიძლიათ უნივერსიტეტში ჩარიცხვა!")
else:
    print("თქვენ ვერ ჩაეწერებით უნივერსიტეტში!")






name = input("შეიყვანეთ თქვენი სახელი: ")
age = int(input("შეიყვანეთ თქვენი ასაკი: "))
height = float(input("შეიყვანეთ თქვენი სიმაღლე; "))

my_name = "გიორგი"

if age > 18 and name == my_name and height > 1.80:
    print("სწორია")
else:
    print("სამწუხაროდ არა")
    