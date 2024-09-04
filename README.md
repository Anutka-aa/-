calls = 0
def count_calls():  #задаем функцию count_calls
    global calls    #берем переменную calls из глобального пространства
    calls += 1      #счетчик, увеличивает на 1 при каждом выполнении функции

def string_info(string): #задаем функцию string_info
    stroka = str(string)  #задаем тип переменной
    result = (len(stroka), stroka.upper(), stroka.lower())  #определяем результат(количество символов строки, строка в верхнем регистре, строка в нижнем регистре)
    count_calls()  #счетсик функций
    return result  #возвращаем результат

def is_contains(string, list_to_search): #задаем функцию is_contains
    string = str(string).lower()  #задаем тип переменной и преобразуем строку в нижний регистр
    list_to_search = list(list_to_search)  #задаем тип списку
    count_calls()  #счетчик функций
    for i in range(len(list_to_search)):  #делаем список для проверки знаений
        if str(list_to_search[i].lower()) == string: # задаем условие
            result = True  # результат тру
            break  # коней выполнения функции
        else:
            result = False  # иначе фалс
            continue  # продолжается проверка
    return result  # вывод результата

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches

print(calls) #вывод счетчика
