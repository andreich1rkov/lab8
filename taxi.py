while True:
    try:
        N = int(input("Введите число сотрудников от 1 до 1000: "))
        if N < 1 or N > 1000:
            raise ValueError
        break
    except ValueError:
        print("Ошибка, введите число сотрудников от 1 до 1000: ") 
print(N)

for i in range(1,N):
    n1 = int(input(print("Введите расстояние в км до дома 1-го сотрудника")))

