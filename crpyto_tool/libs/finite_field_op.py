# Finite Field 2^8 where p(x) = x^8 + x^4 + x^3 + x + 1
class FiniteFieldNumber:
    # p(x) = x^8 + x^4 + x^3 + x + 1
    magical_number = int('100011011', 2)

    def __init__(self, value, is_bin=True):
        if is_bin:
            self.integer_32bits = int(value, 2)
        else:
            self.integer_32bits = value

    def __lt__(self, other):
        return self.integer_32bits < other.integer_32bits

    def __add__(self, other):
        return FiniteFieldNumber(self.integer_32bits ^ other.integer_32bits, False)

    def __sub__(self, other):
        return FiniteFieldNumber(self.integer_32bits ^ other.integer_32bits, False)

    # multiplication on GF(2^8)
    def __mul__(self, other):
        bin_str = bin(self.integer_32bits)
        new_int32 = int(0)
        for index in range(0, len(bin_str)):
            order_num = len(bin_str) - 1 - index
            if (bin_str[index]) == '1':
                new_int32 ^= other.integer_32bits << order_num
        return FiniteFieldNumber(new_int32, False) % FiniteFieldNumber(FiniteFieldNumber.magical_number, False)

    def __div__(self, other):
        ret_integer_num = int(0)
        tmp_finite_field_num = FiniteFieldNumber(self.integer_32bits, False)
        while tmp_finite_field_num > other:
            tmp_whole_len = len(bin(tmp_finite_field_num.integer_32bits))
            other_whole_len = len(bin(other.integer_32bits))
            tmp_finite_field_num = tmp_finite_field_num - FiniteFieldNumber(
                other.integer_32bits << (tmp_whole_len - other_whole_len), False)
            ret_integer_num ^= 1 << (tmp_whole_len - other_whole_len)
        return FiniteFieldNumber(ret_integer_num, False)

    def __mod__(self, other):
        tmp_finite_field_num = FiniteFieldNumber(self.integer_32bits, False)
        while tmp_finite_field_num > other:
            tmp_whole_len = len(bin(tmp_finite_field_num.integer_32bits))
            other_whole_len = len(bin(other.integer_32bits))
            tmp_finite_field_num = tmp_finite_field_num - FiniteFieldNumber(
                other.integer_32bits << (tmp_whole_len - other_whole_len), False)
        return tmp_finite_field_num

    def __str__(self):
        bin_str = bin(self.integer_32bits)[2:]

        ret_arr = []
        for index in range(0, len(bin_str)):
            order_num = len(bin_str) - 1 - index
            if (bin_str[index]) == '1':
                ret_arr.append('x^' + str(order_num))
        return ' + '.join(ret_arr)
