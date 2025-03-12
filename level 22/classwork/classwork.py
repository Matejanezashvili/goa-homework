#1) კომენტარის სახით დაწერეთ, elif statement-ის სრული ფურმა და ახსენით თუ რა შემთხვევაში ვიყენებთ მას.

# elif-ს ვიყენებთ მაშინ როდესაც გვაქვს რამდენიმე პირობა შესამოწმებელი

#2) დაწერეთ ისეთი პირობა, რომლისთვისაც მხოლოდ if statement-ია საჭირო.

age = int(input("enter age: "))

if age>18:
    print("შენ სრულწლოვანი ხარ!")

#3) ცვლადში შეინახეთ თქვენი საყვარელი ფილმის სახელი, შემდეგ კი მომხმარებელს შემოატანინეთ მისი საყვარელი ფილმი. იმ შემთხვევაში თუ თქვენი და მომხმარებლის საყვარელი ფილმები ემთხვევა - გამოიტანეთ "our movie taste is similar", სხვა შემთხვევაში კი გამოიტანეთ "we like different movies"

my_movie = "capitan america"

user_movie = input("enter your movie: ")

if my_movie==user_movie:
    print("our movie taste is similar")
else:
    print("we like different movies")