def count_numbers_and_strings(data):
    total_sum = 0
    total_length = 0

    if isinstance(data, int):
        total_sum += data
    elif isinstance(data, str):
        total_length += len(data)
    elif isinstance(data, (list, tuple)):
        for item in data:
            sum_, length = count_numbers_and_strings(item)
            total_sum += sum_
            total_length += length
    elif isinstance(data, dict):
        for value in data.values():
            sum_, length = count_numbers_and_strings(value)
            total_sum += sum_
            total_length += length

    return total_sum, total_length


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

total_sum, total_length = count_numbers_and_strings(data_structure)
print("Сумма всех чисел:", total_sum)
print("Сумма длин всех строк:", total_length)
