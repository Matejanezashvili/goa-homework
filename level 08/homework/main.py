# 1)ჩაწერე განსხვავებული მონაცემთა ტიპების (int, float, string, boolean) ცვლადები.

int1 = 10
float1 = 1.1
str1 = "Mate"
learning_programing = True

# 2)მომხმარებელს შემოატანინეთ მისი ასაკი და type() ფუნქციით შეამოწმეთ,თუ რა ტიპის მონაცემია შემოტანილი ასაკი.

age = int(input("Enter Your age: "))
print(type(age))

# 3)მომხმარებელს შემოატანინე მისი ასაკი და ბოლოს დაბეჭდე თუ რამდენი წლის იქნება ის 5 წლის შემდეგ

age = int(input("Enter your age: "))

result = age + 5

print(result)

# 4)მომხმარებელს შემოატანინეთ სახელი გვარი ასაკი სიმაღლე საყვარელი ფერი და გამოიტანეთ ეს ყველაფერი ერთ დიდ წინადადებაში.

name = input("Enter your name: ")
lastname = input("Enter your lastname: ")
age = input("Enter your age: ")
height = input("Enter your height: ")
fav_color = input("Enter your fav color: ")

print(f"My name is: {name}. My lastname is: {lastname}. My age is: {age}. My height is: {height}. My fav color is: {fav_color}.")