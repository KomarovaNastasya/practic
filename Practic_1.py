import random

# 1 задача
my_name = "Настасья"
print(my_name)
# 2 задача
my_age = 18
print(f"Меня зовут {my_name}. Мне {my_age} лет.")
# 3 задача
my_name_x5 = (my_name + " ") * 5
print(f"Для усвоения: {my_name_x5}\n")

# 4, 5, 9 задачи
user_name = input("Как ваше имя? ")
if " " in user_name:
    print("Красивое. Но пробел явно лишний, давайте уберём его.")
    user_name = user_name.replace(' ', '')
print(f"Hola, {user_name}!")
user_age = int(input("А сколько вам лет? "))
if (user_age >= 0) and (user_age <= 7):
    print("Тебе рановато в вузе быть.")
elif (user_age > 7) and (user_age <= 17):
    print("ЕГЭ настигает, у-уу.")
elif (user_age > 17) and (user_age <= 30):
    print(f"Tienes {user_age} años!")
elif (user_age < 0) or (user_age > 150):
    print("Вы нереальны! Но, возможно, вы ошиблись, когда вводили свой возраст.")
else:
    print("Забудем про мой вопрос! Возраст – всего лишь цифра.")

# 6, 7, 8 задача
print("\nПоиграем с вашим именем:")
print("Со второго символа до предпоследнего: " + user_name[1:-1:])
print("Задом наперёд: " + user_name[::-1])
print("Последние три: " + user_name[-3::])
print("Первые пять: " + user_name[:5:])
print(f"Длина имени: {len(user_name)}")
print("В нижнем регистре: " + user_name.lower())
print("В верхнем регистре: " + user_name.upper())
print("Со строчной в верхнем: " + user_name.lower().title().swapcase())
print("С заглавной в нижнем: " + user_name.lower().title())
print("\nА теперь с возрастом:")
print(f"Сумма цифр возраста:  {sum(map(int, str(user_age)))}")
prod_age = 1
age = map(int, str(user_age))
for x in age:
    prod_age *= x
print(f"Произведение цифр возраста: {prod_age}")

# 10 задача
print("\nТеперь, решите выражение:")
num = [random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10)]
answer = num[0] + num[1] * num[2] - num[3]
# print(answer)
user_answer = int(input(f"{num[0]} + {num[1]} * {num[2]} - {num[3]} = "))
if user_answer == answer:
    print("Да вы математик!")
else:
    print("Увы, это неверно.")
