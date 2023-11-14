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


# Ввод N
N = Obrabotka_N()


# Ввод км до хат сотрудников
distances = []
for i in range(N):
    print(f"Введите расстояние в километрах для сотрудника {i}: ")
    distance = Obrabotka_KM_and_Tarifs()
    distances.append(distance)
print()


# Ввод тарифов для бомбин
Tarifs = []
for i in range(N):
    print(f"Ввердите тариф для таксиста {i}: ")
    Tarif = Obrabotka_KM_and_Tarifs()
    Tarifs.append(Tarif)
print()



# Главные функции (сортировка бомбин для сотрудников)
# MAIN ИДЕЯ: 
# берем мин. элемент из distances и ему в пару даём макс. элемент из Tarifs.
# Далее убираем эти 2 элемента из списков и повторяем процедуру.

Prices = []
while distances != [] and Tarifs != []:
    for i in range(N):


print(min(distances))
print(min(Tarifs))
