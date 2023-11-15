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
            if X < 1:
                raise ValueError
            break
        except ValueError:
            print("Ошибка, введите целое положительное число: ")
    return X

# max число = 100000
def Number_to_Text(enterNumber):
    if enterNumber <= 0 or enterNumber > 100000:
        print("Число не входит в диапазон от 1 до 100000!", end="")

    if enterNumber == 100000:
        print("Сто тысяч ", end="")


    if (enterNumber // 10000) % 10 == 1:
        print("Десять ", end="")
    if (enterNumber // 10000) % 10 == 2:
        print("Двадцать ", end="")
    elif (enterNumber // 10000) % 10 == 3:
        print("Тридцать ", end="")
    elif (enterNumber // 10000) % 10 == 4:
        print("Сорок ", end="")
    elif (enterNumber // 10000) % 10 == 5:
        print("Пятьдесят ", end="")
    elif (enterNumber // 10000) % 10 == 6:
        print("Шестьдесят ", end="")
    elif (enterNumber // 10000) % 10 == 7:
        print("Семьдесят ", end="")
    elif (enterNumber // 10000) % 10 == 8:
        print("Восемьдесят ", end="")
    elif (enterNumber // 10000) % 10 == 9:
        print("Девяносто ", end="")


    if (enterNumber // 1000) % 10 == 1:
        print("Одна тысяча ", end="")
    elif (enterNumber // 1000) % 10 == 2:
        print("Две тысячи ", end="")
    elif (enterNumber // 1000) % 10 == 3:
        print("Три тысячи ", end="")
    elif (enterNumber // 1000) % 10 == 4:
        print("Четыре тысячи ", end="")
    elif (enterNumber // 1000) % 10 == 5:
        print("Пять тысяч ", end="")
    elif (enterNumber // 1000) % 10 == 6:
        print("Шесть тысяч ", end="")
    elif (enterNumber // 1000) % 10 == 7:
        print("Семь тысяч ", end="")
    elif (enterNumber // 1000) % 10 == 8:
        print("Восемь тысяч ", end="")
    elif (enterNumber // 1000) % 10 == 9:
        print("Девять тысяч ", end="")


    if (enterNumber // 100) % 10 == 1:
        print("сто ", end="")
    elif (enterNumber // 100) % 10 == 2:
        print("двести ", end="")
    elif (enterNumber // 100) % 10 == 3:
        print("триста ", end="")
    elif (enterNumber // 100) % 10 == 4:
        print("четыреста ", end="")
    elif (enterNumber // 100) % 10 == 5:
        print("пятьсот ", end="")
    elif (enterNumber // 100) % 10 == 6:
        print("шестьсот ", end="")
    elif (enterNumber // 100) % 10 == 7:
        print("семьсот ", end="")
    elif (enterNumber // 100) % 10 == 8:
        print("восемьсот ", end="")
    elif (enterNumber // 100) % 10 == 9:
        print("девятьсот ", end="")


    if (enterNumber // 10) % 10 == 1:
        if enterNumber % 10 == 0:
            print("десять рублей", end="")
        elif enterNumber % 10 == 1:
            print("одинадцать рублей", end="")
        elif enterNumber % 10 == 2:
            print("двенадцать рублей", end="")
        elif enterNumber % 10 == 3:
            print("тринадцать рублей", end="")
        elif enterNumber % 10 == 4:
            print("четырнадцать рублей", end="")
        elif enterNumber % 10 == 5:
            print("пятнадцать рублей", end="")
        elif enterNumber % 10 == 6:
            print("шестнадцать рублей", end="")
        elif enterNumber % 10 == 7:
            print("семнадцать рублей", end="")
        elif enterNumber % 10 == 8:
            print("восемнадцать рублей", end="")
        else:
            print("девятнадцать рублей", end="")
        

    if ((enterNumber // 10) % 10 == 2):
        print("двадцать ", end="")
    elif ((enterNumber // 10) % 10 == 3):
        print("тридцать ", end="")
    elif ((enterNumber // 10) % 10 == 4):
        print("сорок ", end="")
    elif ((enterNumber // 10) % 10 == 5):
        print("пятьдесят ", end="")
    elif ((enterNumber // 10) % 10 == 6):
        print("шестьдесят ", end="")
    elif ((enterNumber // 10) % 10 == 7):
        print("семьдесят ", end="")
    elif ((enterNumber // 10) % 10 == 8):
        print("восемьдесят ", end="")
    elif ((enterNumber // 10) % 10 == 9):
        print("девяносто ", end="")


    if (enterNumber // 10) % 10 != 1:
        if enterNumber % 10 == 0:
            print("рублей", end="")
        elif enterNumber % 10 == 1:
            print("один рубль", end="")
        elif enterNumber % 10 == 2:
            print("два рубля ", end="")
        elif enterNumber % 10 == 3:
            print("три рубля", end="")
        elif enterNumber % 10 == 4:
            print("четыре рубля", end="")
        elif enterNumber % 10 == 5:
            print("пять рублей", end="")
        elif enterNumber % 10 == 6:
            print("шесть рублей", end="")
        elif enterNumber % 10 == 7:
            print("семь рублей", end="")
        elif enterNumber % 10 == 8:
            print("восемь рублей", end="")
        else:
            print("девять рублей", end="")


# Ввод N
N = Obrabotka_N()

# Пробел
print() 



# Ввод км до домов сотрудников
distances = []
for i in range(N):
    print(f"Введите расстояние в километрах для сотрудника {i+1}: ", end=" ")
    distance = Obrabotka_KM_and_Tarifs()
    distances.append(distance)
print()


# Ввод тарифов для таксистов
Tarifs = []
for i in range(N):
    print(f"Ввердите тариф для таксиста {i+1}: ", end=" ")
    Tarif = Obrabotka_KM_and_Tarifs()
    Tarifs.append(Tarif)
print()


# берем мин. элемент из distances и ему в пару даём макс. элемент из Tarifs.
# Далее убираем эти 2 элемента из списков и повторяем.
Prices = []
FinalList = []
while distances != [] and Tarifs != []:
    for i in range(N):
        Km = min(distances)
        Price = max(Tarifs)
        Price_za_Kms = Km*Price
        distances.remove(Km)
        Tarifs.remove(Price)
        Prices.append([i+1, Price_za_Kms])
        FinalList.append([Km, Price])


# Список сотрудников с их километрами
print("Список сотрудников: 1-е число - номер сотрудника (начиная с '1'), 2-е число - сумма за такси до его дома:")
print(Prices)
print()
print("Список км и тарифов: 1-е число - расстояние в километрах, 2-е число - тариф такси, который этому расстоянию соответсвует:")
print(FinalList)
print()

# Определение итоговой суммы
y = []
for i in range(N):
    y.append(Prices[i][1])
    i += 1


# Число в текст
number = sum(y)
print(f"Общая минимальная сумма для заказа такси для всех сотрудников: {number} руб.", end=" ")
Number_to_Text(number)







