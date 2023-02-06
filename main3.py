# задача 1
month = 0
while month > 12 or month < 1:
    month = int(input("Введите номер месяца: "))
season_to_months = {"Весна": [3, 4, 5], "Лето": [6, 7, 8], "Осень": [9, 10, 11], "Зима": [12, 1, 2]}
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]
winter = [12, 1, 2]
if month in spring:
    print("Результат через список: Весна")
elif month in summer:
    print("Результат через список: Лето")
elif month in autumn:
    print("Результат через список: Осень")
else:
    print("Результат через список: Зима")
for season in season_to_months.keys():
    if month in season_to_months.get(season):
        print(f"Результат через словарь: {season}")
# задача 2

words = input("Введите слова через пробел:").split(" ")
n = 0
for word in words:
    n += 1
    if len(word) <= 10:
        print(f"{n}. {word} ")
    else:
        print(f"{n}. {word[:10]}")

# задача 3
my_list = [7, 5, 3, 3, 2]
num = int(input("Введите натуральное число:"))
my_list.append(num)
my_list.sort()
my_list.reverse()
print(*my_list)

# задача 4
inp = "да"
n = 0
list_of_tuples = []
names = []
prices = []
quantities = []
items = []
while inp == "да":
    n += 1
    inp = input("Хотите внести информацию о товаре?")
    if inp == "нет":
        break
    name = input("Введите название")
    if name not in names:
        names.append(name)
    price = int(input("Введите цену"))
    prices.append(price)
    quantity = int(input("Введите количество"))
    quantities.append(quantity)
    item = input("Введите название единицы товара")
    if item not in items:
        items.append(item)
    dictionary = {"название": name, "цена": price, "количество": quantity, "eд": item}
    tuple = (n, dictionary)
    list_of_tuples.append(tuple)
print(list_of_tuples)
analytics = {"названия":names, "цены":prices, "количества":quantities, "ед":items}
print(analytics)
# задача 5
