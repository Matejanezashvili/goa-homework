#upper-ს uppercase-ში გადაყავს სთრინგი lower-ს lowercase-ში ხოლო capitalize-ში მარტო საწყისი ასო არის აფერქეისში
name=input("your name: ")
if name[0].isupper():
    print("Hello")
else: print("Bye")
surname=input("enter surname: ")
if surname[0].lower() == "m":
    print(surname.upper())
elif surname[0].lower() == "g":
    print(surname.lower())

color=input("Whats ur fav color?: ")
if color[0].lower() == "p":
    print("Gamarjoba")
else: print("Naxvamdis")