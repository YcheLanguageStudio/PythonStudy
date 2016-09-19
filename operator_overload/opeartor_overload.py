# Finite Field 2^8 where p(x) = x^8 + x^4 +x x^3 + x + 1
class FiniteFieldNumber:
    def __init__(self, value, is_bin=True):
        if is_bin:
            self.integer_32bits = int(value, 2)
        else:
            self.integer_32bits = value
        self.px_integer_32bits = int('100011011', 2)

    def __mod__(self, other):
        return

    def __mul__(self, other):
        return

    def __add__(self, other):
        return FiniteFieldNumber(self.integer_32bits ^ other.integer_32bits, False)

    def __sub__(self, other):
        return FiniteFieldNumber(self.integer_32bits ^ other.integer_32bits, False)

    def __str__(self):
        bin_str = bin(self.integer_32bits)
        whole_len = len(bin_str)
        ret_str = str()
        start_flag = False
        for index in range(0, whole_len):
            order_num = whole_len - 1 - index
            if (bin_str[index]) == '1':
                if start_flag:
                    ret_str += ' + '
                else:
                    start_flag = True
                ret_str += 'x^' + str(order_num)
        return ret_str


if __name__ == '__main__':
    number2 = FiniteFieldNumber('0');
    number3 = FiniteFieldNumber('1000110');
    print number2 - number3

    number0 = FiniteFieldNumber('1000110')
    number1 = FiniteFieldNumber('10001011')
    print number0 + number1
