# Дана строка (возможно, пустая), состоящая из букв A-Z: AAAABBBCCXYZDDDDEEEFFFAAAAAABBBB BBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE, которая на выходе даст строку вида: A4B3C2XYZD4E3F3A6B28 
# и сгенерирует ошибку, если на вход пришла невалидная строка.
# Пояснения: Если символ встречается 1 раз, он остается без изменений;
# Если символ повторяется более 1 раза, к нему добавляется количество повторений.

def convert_string(input_str):

    prev_symbol = None
    len_of_series = 0
    result = ""

    for symb in input_str:
        if prev_symbol and symb != prev_symbol:
            result = result + f"{prev_symbol}{len_of_series}"
            len_of_series = 1
        else:
            len_of_series += 1

        prev_symbol = symb

    return result + f"{prev_symbol}{len_of_series}" if prev_symbol else ""


input_str = str(input("Введите буквы: "))
print(input_str + " -> " + convert_string(input_str))

