def get_number_input(prompt): #для проверки является ли введеное значение числом
    while True:
        user_input = input(prompt)
        try:
            number = float(user_input)
            return number
        except ValueError:
            print("Введено не число, попробуйте снова.")

print('Введите количество сотрудников:')
n = get_number_input('')
print('Введите расстояния в километрах до домов сотрудников от дома:')
km = input()
mas_km = []
print('Введите стоимость такси за километр')
cell = input()
mas_cell= []
proverka = mas_cell
km = km.split()
for i in km:
    mas_km.append(int(i))
cell = cell.split()
for j in cell:
    mas_cell.append(int(j))
print(mas_km, mas_cell)

mas_cell.sort()
mas_km.sort(reverse=True)

print(mas_km, mas_cell)
for q in range(len(mas_km)):
    res = mas_km[q] * mas_cell[q]
    print(res)
print(proverka)