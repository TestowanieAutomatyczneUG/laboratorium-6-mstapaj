def roman(number):
    result = ''
    temp = number
    while temp != 0:
        if temp >= 900:
            if 1000 > temp >= 900:
                result += 'CM'
                temp -= 900
            else:
                temp -= 1000
                result += 'M'
        elif temp >= 400:
            if 500 > temp >= 400:
                temp -= 400
                result += 'CD'
            else:
                temp -= 500
                result += 'D'
        elif temp >= 90:
            if 100 > temp >= 90:
                temp -= 90
                result += 'XC'
            else:
                temp -= 100
                result += 'C'
        elif temp >= 40:
            if 50 > temp >= 40:
                temp -= 40
                result += 'XL'
            else:
                temp -= 50
                result += 'L'
        elif temp >= 9:
            if temp == 9:
                temp -= 9
                result += 'IX'
            else:
                temp -= 10
                result += 'X'
        elif temp >= 4:
            if temp == 4:
                temp -= 4
                result += 'IV'
            else:
                temp -= 5
                result += 'V'

        elif temp > 0:
            result += 'I' * temp
            temp = 0
    return result
