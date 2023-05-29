SEPARATOR = '------------------------------------------'

name = ''
age = 0
phone = ''
email = ''
index = ''
post_address = ''
information = ''
state_number = 0
tax_number = 0
payment_account = 0
name_bank = ''
code = 0
score = 0


def general_info_user(name_parameter, age_parameter, ph_parameter, email_parameter, index_parameter, post_address_parameter, information_parameter):
    print(SEPARATOR)
    print('Имя:    ', name_parameter)

    if 11 <= age_parameter % 100 <= 19:
        years_parameter = 'лет'

    elif age_parameter % 10 == 1:
        years_parameter = 'год'

    elif 2 <= age_parameter % 10 <= 4:
        years_parameter = 'года'

    else:
        years_parameter = 'лет'

    print('Возраст:', age_parameter, years_parameter)
    print('Телефон:', ph_parameter)
    print('E-mail: ', email_parameter)
    print('Индекс: ', index_parameter)
    print('Адрес:  ', post_address_parameter)

    if information_parameter:
        print('')
        print('Дополнительная информация:')
        print(information_parameter)


def business(state_number_parameter, tax_number_parameter, payment_account_parameter, name_bank_parameter, code_parameter, score_parameter):
    print('Информация о предпринимателе:')
    print('ОГРНИП:', state_number_parameter)
    print('ИНН:   ', tax_number_parameter)
    print()
    print('Банковские реквизиты:')
    print('Р/с:   ', payment_account_parameter)
    print('Банк:  ', name_bank_parameter)
    print('БИК:   ', code_parameter)
    print('К/с:   ', score_parameter)


def counter(number):
    num_long = 0

    while number > 0:
        number //= 10
        num_long += 1

    return num_long


print('Приложение MyProfile')
print('Сохраняй информацию о себе и выводи ее в разных форматах')

while True:
    print(SEPARATOR)
    print('ГЛАВНОЕ МЕНЮ')
    print('1 - Ввести или обновить информацию')
    print('2 - Вывести информацию')
    print('0 - Завершить работу')

    option = int(input('Введите номер пункта меню: '))

    if option == 0:
        break

    elif option == 1:

        while True:
            print(SEPARATOR)
            print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
            print('1 - Личная информация')
            print('2 - Информация о предпринимателе')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))

            if option2 == 0:
                break

            elif option2 == 1:
                name = input('Введите имя: ')

                while 1:
                    age = int(input('Введите возраст: '))

                    if age > 0:
                        break

                    print('Возраст должен быть положительным')

                uph = input('Введите номер телефона (+7ХХХХХХХХХХ): ')

                for ch in uph:

                    if ch == '+' or ('0' <= ch <= '9'):
                        phone += ch

                email = input('Введите адрес электронной почты: ')

                while 1:
                    index = input('Введите почтовый индекс: ')
                    filters = index
                    symbol = '1234567890'
                    final_filter = ''

                    for i in filters:

                        for _ in symbol:

                            if i == _:
                                final_filter += i

                    index = final_filter
                    break

                post_address = input('Введите почтовый адрес (без индекса): ')
                information = input('Введите дополнительную информацию:\n')

            elif option2 == 2:

                while 1:
                    state_number = int(input('Введите ОГРНИП: '))
                    count = counter(state_number)

                    if count < 15:
                        print('ОГРНИП должен содержать 15 цифр')

                    else:
                        break

                tax_number = int(input('Введите ИНН: '))

                while 1:
                    payment_account = int(input('Введите расчётный счёт: '))
                    count = counter(payment_account)

                    if count < 20:
                        print('Расчетный счет должен содержать 20 цифр')

                    else:
                        break

                name_bank = input('Введите название банка: ')
                code = int(input('Введите БИК: '))
                score = int(input('Введите корреспондентский счет: '))

            else:
                print('Введите корректный пункт меню')

    elif option == 2:

        while True:
            print(SEPARATOR)
            print('ВЫВЕСТИ ИНФОРМАЦИЮ')
            print('1 - Личная информация')
            print('2 - Вся информация')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))

            if option2 == 0:
                break

            elif option2 == 1:
                general_info_user(name, age, phone, email, index, post_address, information)

            elif option2 == 2:
                general_info_user(name, age, phone, email, index, post_address, information)
                print()
                business(state_number, tax_number, payment_account, name_bank, code, score)

            else:
                print('Введите корректный пункт меню')

    else:
        print('Введите корректный пункт меню')
