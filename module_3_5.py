def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

result = get_multiplied_digits(12345)
print(result)

result2 = get_multiplied_digits(6789)
print(result2)

result3 = get_multiplied_digits(10345)
print(result3)

result4 = get_multiplied_digits(40203)
print(result4)
