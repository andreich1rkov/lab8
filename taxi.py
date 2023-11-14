def Obrabotka_N():
    while True:
        try:
            N = int(input("Введите число сотрудников от 1 до 1000: "))
            if N < 1 or N > 1000:
                raise ValueError
            break
        except ValueError:
            print("Ошибка, введите число сотрудников от 1 до 1000: ")
    return N

def Obrabotka_KM_and_Tarifs():
    while True:
        try:
            X = int(input())
            if X < 0:
                raise ValueError
            break
        except ValueError:
            print("Ошибка, введите целое положительное число: ")
    return X

def Number_to_Text(enterNumber):
    if enterNumber <= 0 or enterNumber > 100000:
        print("Число не входит в диапазон от 1 до 100000!")

    if enterNumber == 100000:
        print("Сто тысяч ")


    if (enterNumber // 10000) % 10 == 1:
        print("Десять ")
    if (enterNumber // 10000) % 10 == 2:
        print("Двадцать ")
    elif (enterNumber // 10000) % 10 == 3:
        print("Тридцать ")
    elif (enterNumber // 10000) % 10 == 4:
        print("Сорок ")
    elif (enterNumber // 10000) % 10 == 5:
        print("Пятьдесят ")
    elif (enterNumber // 10000) % 10 == 6:
        print("Шестьдесят ")
    elif (enterNumber // 10000) % 10 == 7:
        print("Семьдесят ")
    elif (enterNumber // 10000) % 10 == 8:
        print("Восемьдесят ")
    elif (enterNumber // 10000) % 10 == 9:
        print("Девяносто ")


    if (enterNumber // 1000) % 10 == 1:
        print("Одна тысяча ")
    elif (enterNumber // 1000) % 10 == 2:
        print("Две тысячи ")
    elif (enterNumber // 1000) % 10 == 3:
        print("Три тысячи ")
    elif (enterNumber // 1000) % 10 == 4:
        print("Четыре тысячи ")
    elif (enterNumber // 1000) % 10 == 5:
        print("Пять тысяч ")
    elif (enterNumber // 1000) % 10 == 6:
        print("Шесть тысяч ")
    elif (enterNumber // 1000) % 10 == 7:
        print("Семь тысяч ")
    elif (enterNumber // 1000) % 10 == 8:
        print("Восемь тысяч ")
    elif (enterNumber // 1000) % 10 == 9:
        print("Девять тысяч ")


    if (enterNumber // 100) % 10 == 1:
        print("сто ")
    elif (enterNumber // 100) % 10 == 2:
        print("двести ")
    elif (enterNumber // 100) % 10 == 3:
        print("триста ")
    elif (enterNumber // 100) % 10 == 4:
        print("четыреста ")
    elif (enterNumber // 100) % 10 == 5:
        print("пятьсот ")
    elif (enterNumber // 100) % 10 == 6:
        print("шестьсот ")
    elif (enterNumber // 100) % 10 == 7:
        print("семьсот ")
    elif (enterNumber // 100) % 10 == 8:
        print("восемьсот ")
    elif (enterNumber // 100) % 10 == 9:
        print("девятьсот ")


    if (enterNumber // 10) % 10 == 1:
        if enterNumber % 10 == 0:
            print("десять рублей")
        elif enterNumber % 10 == 1:
            print("одинадцать рублей")
        elif enterNumber % 10 == 2:
            print("двенадцать рублей")
        elif enterNumber % 10 == 3:
            print("тринадцать рублей")
        elif enterNumber % 10 == 4:
            print("четырнадцать рублей")
        elif enterNumber % 10 == 5:
            print("пятнадцать рублей")
        elif enterNumber % 10 == 6:
            print("шестнадцать рублей")
        elif enterNumber % 10 == 7:
            print("семнадцать рублей")
        elif enterNumber % 10 == 8:
            print("восемнадцать рублей")
        else:
            print("девятнадцать рублей")
        

    if ((enterNumber // 10) % 10 == 2):
        print("двадцать ")
    elif ((enterNumber // 10) % 10 == 3):
        print("тридцать ")
    elif ((enterNumber // 10) % 10 == 4):
        print("сорок ")
    elif ((enterNumber // 10) % 10 == 5):
        print("пятьдесят ")
    elif ((enterNumber // 10) % 10 == 6):
        print("шестьдесят ")
    elif ((enterNumber // 10) % 10 == 7):
        print("семьдесят ")
    elif ((enterNumber // 10) % 10 == 8):
        print("восемьдесят ")
    elif ((enterNumber // 10) % 10 == 9):
        print("девяносто ")


    if (enterNumber // 10) % 10 != 1:
        if enterNumber % 10 == 0:
            print("рублей")
        elif enterNumber % 10 == 1:
            print("один рубль")
        elif enterNumber % 10 == 2:
            print("два рубля ")
        elif enterNumber % 10 == 3:
            print("три рубля")
        elif enterNumber % 10 == 4:
            print("четыре рубля")
        elif enterNumber % 10 == 5:
            print("пять рублей")
        elif enterNumber % 10 == 6:
            print("шесть рублей")
        elif enterNumber % 10 == 7:
            print("семь рублей")
        elif enterNumber % 10 == 8:
            print("восемь рублей")
        else:
            print("девять рублей")


# Ввод N
N = Obrabotka_N()


# Ввод км до домов сотрудников
distances = []
for i in range(N):
    print(f"Введите расстояние в километрах для сотрудника {i}: ")
    distance = Obrabotka_KM_and_Tarifs()
    distances.append(distance)
print()


# Ввод тарифов для таксистов
Tarifs = []
for i in range(N):
    print(f"Ввердите тариф для таксиста {i}: ")
    Tarif = Obrabotka_KM_and_Tarifs()
    Tarifs.append(Tarif)
print()


# берем мин. элемент из distances и ему в пару даём макс. элемент из Tarifs.
# Далее убираем эти 2 элемента из списков и повторяем.
Prices = []
while distances != [] and Tarifs != []:
    for i in range(N):
        Km = min(distances)
        Price = max(Tarifs)
        Price_za_Kms = Km*Price
        distances.remove(Km)
        Tarifs.remove(Price)
        Prices.append([Km, Price_za_Kms])

print(Prices)


# Итоговая сумма
y = []
for i in range(N):
    y.append(Prices[i][1])
    i += 1
print(f"{sum(y)} руб.\n")


# Число в текст
number = sum(y)
Number_to_Text(number)



