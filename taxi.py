def get_number_input(prompt):#для проверки является ли введеное значение числом
    while True:
        user_input = input(prompt)
        try:
            number = float(user_input)
            return number
        except ValueError:
            print("Введено не число, попробуйте снова.")

print('Введите количество сотрудников:')
n = get_number_input('')