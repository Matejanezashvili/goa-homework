# 1)
from builtins import list, print, range


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
first_five = numbers[:5]

print(first_five)
# 2)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

first_five_numbers = numbers[:5]

print(first_five_numbers)

numbers_20_to_30 = list(range(20, 31))

even_numbers = numbers_20_to_30[::2]
# 3)
sentence = "Goal-Oriented Academy"

academy = sentence[-7:]

print(academy)
# 4)
for i in range(5):
    print(i)

numbers = list(range(5))
print(numbers)
print("Hello, World!")
# 5)
# 1. კოდის გამარტივება და გაწმენდა: ფუნქციები იძლევა საშუალებას დავაბზაროთ კოდი პატარა, ახსნაანუ ნაწილებად, რაც უფრო მარტივად აკონტროლებადი და გასაგებია.
# 2. გადამოწმება და ხელახლა გამოყენება: ფუნქციებს შეგვიძლია მრავალჯერადი გამოყენება სხვადასხვა ადგილებში, რაც ამცირებს კოდის გამეორებას.
# 3. შეცდომების აღმოჩენა და ოპტიმიზაცია: ფუნქციები ქმნიან ქაფს, რომელშიც შეიძლება იყოს ერთი კონკრეტული ლოგიკა, რაც უმარტივესად გვაძლევს შეცდომების გამოსწორებას.
