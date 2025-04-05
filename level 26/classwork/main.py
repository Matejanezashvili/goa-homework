# 1) ცვლადში შეინახეთ თქვენი გვარი. ინდექსინგის საშუალებით გამოიტანეთ თქვენი გვარის პირველი, ბოლო და შუა ასოები.

from builtins import print


my_username = "janezashvili"
print(my_username[:4])
print(my_username[4:8])
print(my_username[8:12])

# 2) შეინახე ცვლადში "Hello, World!". Slicing-ის საშუალებით ამ სტრინგიდან  ამოიღეთ ცალკე სიტყვა "Hello" და ცალკე სიტყვა "World!". შეინახეთ ისინი ცვლადებში და გამოიტანეთ ეკრანზე.

hallo = "Hello World!"
print(hallo[:5])
print(hallo[6:12])
Hello_World = ["Hello", "World!"]
print(Hello_World)
# 3) ცვლადში შეინახეთ წინადადება - " makes perfect". შექმენით ახალი ცვლადი, სადაც ამ წინადადების შებრუნებულ ვერსიას შეინახავთ. საბოლოოდ, ამ წინადადების თავდაპირველი და შებრუნებული ვერსიები დაბეჭდეთ ტერმინალში.

original_practice = "practice makes perfect"
inverted_practice = original_practice[::-1]
print([original_practice, inverted_practice])
