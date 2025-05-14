# Функции
# Структура
# def <название функции>(<параметр 1>, <параметр 2>, ...)
def error(message):
    print('You have', message, 'error')


# Вызов функции
# В функцию передаются аргументы
# Сколько параметров, столько и аргументов
error(404)


# Если мы хотим задать значение по умолчанию,
# делаем это при объявлении параметров функции
def welcome_print(name='user'):
    print('Hello,', name)


welcome_print('Artem')


# args - сокращение от слова arguments (аргументы)
# позволяет передать в функцию произвольное количество аргументов
# * - команда распаковки
def print_sum(*args):
    my_sum = 0
    for i in args:
        my_sum += i
    print(my_sum)


print_sum(1, 2, 3, 4)


# kwargs - сокращение от слов key word arguments(именованные аргументы)
# ** - сопоставление ключей из словаря и названий переменных в функции
def print_client_data(name: str, surname: str, age: int, address: str) -> None:
    '''

    :param name: this is client name
    :param surname: this is client surname
    :param age: this is client age
    :param address: this is client address
    :return: None
    '''
    print('Имя клиента:', name)
    print('Фамилия клиента:', surname)
    print('Возраст клиента:', age)
    print('Адрес клиента:', address)


client1 = {'name': 'Artem', 'surname': 'Nesterenko', 'age': 17, 'address': 'KLGD'}
client2 = {'name': 'Artem', 'surname': 'Shigrev', 'age': 16, 'address': 'KLGD'}
client3 = {'name': 'Artem', 'surname': 'Mishunov', 'age': 16, 'address': 'KLGD'}
print_client_data(**client2)
