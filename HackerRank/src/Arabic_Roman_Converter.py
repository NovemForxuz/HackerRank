

def arabic_roman_converter(t):
    result = ''
    temp = t
    while temp != 0:
        if (temp // 1000) != 0:
            result += 'M'
            temp -= 1000
        elif (temp // 900) != 0:
            result += 'CM'
            temp -= 900
        elif (temp // 500) != 0:
            result += 'D'
            temp -= 500
        elif (temp // 400) != 0:
            result += 'CD'
            temp -= 400
        elif (temp // 100) != 0:
            result += 'C'
            temp -= 100
        elif (temp // 90) != 0:
            result += 'XC'
            temp -= 90
        elif (temp // 50) != 0:
            result += 'L'
            temp -= 50
        elif (temp // 40) != 0:
            result += 'XL'
            temp -= 40
        elif (temp // 10) != 0:
            result += 'X'
            temp -= 10
        elif (temp // 9) != 0:
            result += 'IX'
            temp -= 9
        elif (temp // 5) != 0:
            result += 'V'
            temp -= 5
        elif (temp // 4) != 0:
            result += 'IV'
            temp -= 4
        elif (temp // 1) != 0:
            result += 'I'
            temp -= 1
    return result


user_input = int(input("Write a number: "))
print(arabic_roman_converter(user_input))
