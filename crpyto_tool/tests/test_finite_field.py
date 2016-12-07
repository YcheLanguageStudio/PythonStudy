from crpyto_tool.libs.finite_field_op import FiniteFieldNumber

if __name__ == '__main__':
    magical_number = FiniteFieldNumber(FiniteFieldNumber.magical_number, False)
    print 'p(x): ' + str(magical_number)

    number2 = FiniteFieldNumber('0')
    number3 = FiniteFieldNumber('1000110')
    print 'Q5-(1):' + str(number2 - number3)

    number0 = FiniteFieldNumber('1000110')
    number1 = FiniteFieldNumber('10001011')
    print 'Q5-(2):' + str(number0 + number1)

    print 'Q5-(3):' + str(number0 * number1)

    number4 = FiniteFieldNumber('10000111111010')
    print number4 / magical_number

    print FiniteFieldNumber('11110101') * FiniteFieldNumber('1000110')
