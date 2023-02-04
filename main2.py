# задача 1
print("Введите число а")
a = int(input())
print("Введите число b")
b = int(input())
day = 1
while a < b:
    a *= 1.1
    day += 1
print(day)

# задача 2

n = 0
num = 0
while num <= 0:
    print("Введите целое положительное число: ")
    num = int(input())
max = 0
while num >= 1:
    if (num % 10) > max:
        max = num % 10
    num //= 10
print(f"Самая большая цифра в числе: {max}")

# задача 3

lst = [5, "string", 0.15, True, None]
for element in lst:
    print(type(element))

# задача 4

print("Введите целые числа через пробел:")
nums = []
for num in input().split(" "):
    nums.append(int(num))
swapped = []
i = 0
if len(nums) % 2 == 0:
    while i < len(nums):
        swapped.append(nums[i + 1])
        swapped.append(nums[i])
        i += 2
else:
    last = nums[-1]
    nums.remove(last)
    while i < len(nums):
        swapped.append(nums[i + 1])
        swapped.append(nums[i])
        i += 2
    swapped.append(last)
string = ""
for element in swapped:
    string += str(element) + " "
print(f"Результат: {string}")

# задача 5

print("Введите слова через пробел:")
words = input().split(" ")
n = 0
for word in words:
    n += 1
    if len(word) <= 10:
        print(f"{n}. {word} ")
    else:
        print(f"{n}. {word[:10]}")
