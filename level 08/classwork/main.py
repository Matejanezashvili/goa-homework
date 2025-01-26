# 1)მომხმარებელს შემოატანინეთ მისი ასაკი და გარდაქმენით ის სხვადასხვა მონაცემთა ტიპად

age = str(input("Enter your age: ")) # ტექსტი
age = int(input("Enter your age: ")) # მთელი რიცხვი: 5, 10, 20.
age = float(input("Enter your age: ")) # წილადიანი რიცხვი: 10.9 7.9 13.8 
print(type(age))

# 2)ახსენით კომენტარებით რას აკეთებს int(),str() და float() ფუნქციები

# ეს ფუნქციები int(), str(), float(): ცვლის მონაცემთა ტიპს

# 3)მომხმარებელს შემოატანინეთ ასაკი და დაბეჭდეთ თუ რამდენი წლის იქნება 5 წელიწადში

age = int(input("Enter your age: "))

result = age + 5

print(result)