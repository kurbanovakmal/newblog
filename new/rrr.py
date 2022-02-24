# name = input('Введите имя:')
# first_name = input('Введите Фамилию:')
# last_name = input('Введите отчество:')
# a = int(input('Введите год поступления:'))
# b = 2 + a
# print(f"{name} {first_name} {last_name} you are going to graduate in {b}")

numbers = input("enter nums using comma: ").split(",")
sum = 0
for x in numbers:
    sum = sum + int(x)**3
print(sum)
