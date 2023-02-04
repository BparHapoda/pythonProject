# задача 1
print("Введите Ваше имя")
name = input()
print("Введите Ваш пароль")
password = input()
print("Введите Ваш возраст")
age = int(input())
print(f"Ваши данные для входа в аккаунт: имя - {name}, пароль - {password}, возраст - {age}.")

# задача 2

# задача 3

n=0
while n<=0:
    print("Введите целое положительное число n")
    n=int(input())
sum=n + n **  2 + n ** 3
print(f"n + nn + nnn = {sum}")



# задача 4


n=0
while n<=0:
    print("Введите целое положительное число n")
    n=int(input())
sum=n + n **  2 + n ** 3
print(f"n + nn + nnn = {sum}")

print("Введите выручку фирмы")
revenue = int(input())
print("Введите издержки фирмы")
cost = int(input())
if revenue >= cost:
    print(f"Финансовый результат - прибыль. Ее величина: {revenue - cost}")
    print(f"Рентабельность выручки = {cost / revenue}")
    print("Введите численность сотрудников фирмы")
    workers = int(input())
    print(f"Прибыль фирмы в расчете на одного сотрудника = {cost / workers}")
else:
    print(f"Финансовый результат - убыток. Его величина: {revenue - cost}")