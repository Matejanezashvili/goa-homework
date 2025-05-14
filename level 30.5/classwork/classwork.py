
# ცვლადში შეინახეთ თქვენი სახელი, შემდეგ კი მომხმარებელსაც შემოატანინეთ თავისი სახელი, თუ თქვენი სახელები დაემთხვევა გამოუტანეთ "Our names are
# similar !", სხვა შემთხვევაში - "We have different names". hint: დაგჭირდებათ პირობითი განცხადებები და სტრინგის მეთოდები. ეს შემოწმება უნდა იყოს case-insensitive

my_name = "mate"
user_name = input("Enter your name: ")

if my_name.lower() == user_name.lower():
    print("Our names are similar!")
else:
    print("We have different names.")
