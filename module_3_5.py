def get_multiplied_digits(number):  
    number = int(number)            # убираем нули в начале number
    str_number = str(number)        
    first = int(str_number[0])     

    while str_number.endswith('0'): # убираем нули в конце number
            str_number = str_number[:len(str_number)]
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first
