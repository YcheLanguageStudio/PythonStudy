# Finite Field 2^8 where p(x) = x^8 + x^4 + x^3 + x + 1
class FiniteFieldNumber:
    # p(x) = x^8 + x^4 + x^3 + x + 1
    magical_number = int('100011011', 2)

    def __init__(self, value, is_bin=True):
        if is_bin:
            self.integer = int(value, 2)
        else:
            self.integer = value

    def __lt__(self, other):
        return self.integer < other.integer

    def __add__(self, other):
        return FiniteFieldNumber(self.integer ^ other.integer, False)

    def __sub__(self, other):
        return FiniteFieldNumber(self.integer ^ other.integer, False)

    # multiplication on GF(2^8)
    def __mul__(self, other):
        bin_str = bin(self.integer)
        new_integer = int(0)
        for index in range(len(bin_str)):
            order_num = len(bin_str) - 1 - index
            if (bin_str[index]) == '1':
                new_integer ^= other.integer << order_num
        return FiniteFieldNumber(new_integer, False) % FiniteFieldNumber(FiniteFieldNumber.magical_number, False)

    def __div__(self, other):
        ret_integer = int(0)
        remainder = FiniteFieldNumber(self.integer, False)
        while remainder > other:
            differ_len = len(bin(remainder.integer)) - len(bin(other.integer))
            remainder = remainder - FiniteFieldNumber(other.integer << differ_len, False)
            ret_integer ^= 1 << differ_len
        return FiniteFieldNumber(ret_integer, False)

    def __mod__(self, other):
        remainder = FiniteFieldNumber(self.integer, False)
        while remainder > other:
            differ_len = len(bin(remainder.integer)) - len(bin(other.integer))
            remainder = remainder - FiniteFieldNumber(other.integer << differ_len, False)
        return remainder

    def __str__(self):
        if self.integer == 0:
            return '0'
        else:
            bin_str = bin(self.integer)[2:]
            ret_arr = []
            for index in range(len(bin_str)):
                order_num = len(bin_str) - 1 - index
                if (bin_str[index]) == '1':
                    if order_num != 0:
                        ret_arr.append('x^' + str(order_num))
                    else:
                        ret_arr.append('1')
            return ' + '.join(ret_arr)
