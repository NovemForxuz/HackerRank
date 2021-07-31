
# a function to convert arabic to roman numerals
# takes a single number as parameter, t
def arabic_roman_converter(t):
    result = ''  # store result after each loop
    temp = t     # store remaining value after each loop
    while temp != 0:
        # if value bigger than 1000, division by 1000 will give non-zero
        if (temp // 1000) != 0:
            result += 'M'   # append to result
            temp -= 1000    # re-initialize value

        # else if value is bigger than 900, division by 900 will give non-zero
        elif (temp // 900) != 0:
            result += 'CM'  # append to result
            temp -= 900     # re-initialize value

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

    # return the result after loop end
    return result


# get user input in integer
user_input = int(input("Write a number: "))
# print the result of calling function 'arabic_roman_converter'
print(arabic_roman_converter(user_input))
