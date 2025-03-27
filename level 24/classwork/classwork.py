#1) მომხმარებელს შემოატანინეთ მთელი რიცხვი და დაწერეთ პროგრამა, რომელიც ამოწმებს:
# თუ რიცხვი დადებითია, დაბეჭდოს: "the number is positive"
# თუ უარყოფითია, დაბეჭდოს: "the number is negative"
# თუ ნულია, დაბეჭდოს: "the number is zero"

user_num =int(input("enter your number: "))

if user_num > 0:
    print("the number is positive")
elif user_num < 0:
    print("the number is negative")
else:
    print("the number is zero")
#2) ცვლადში შეინახეთ პაროლი. შემდეგ მომხმარებელს შემოატანინეთ პაროლი. 
# იქამდე გამოუტანეთ "incorrect password" სანამ მომხმარებელი სწორად არ შემოიტანს პაროლს.
#  სწორად გამოტანის შემთხვევაში გამოიტანეთ "correct password" (გამოიყენეთ while loop)

pas = 12345

user_pas = ""

while user_pas != pas:
    user_pas = input("enter your password: ")