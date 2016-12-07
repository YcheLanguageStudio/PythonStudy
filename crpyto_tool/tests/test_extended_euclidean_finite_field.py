from crpyto_tool.libs.extended_euclidean_poly import *
from crpyto_tool.libs.finite_field_op import FiniteFieldNumber

if __name__ == '__main__':
    px_number = FiniteFieldNumber(FiniteFieldNumber.magical_number, False)

    ax_number0 = FiniteFieldNumber('10000011')
    test_extended_gcd_eculidean(px_number, ax_number0)

    print '\n'

    ax_number1 = FiniteFieldNumber('1000110')
    test_extended_gcd_eculidean(px_number, ax_number1)
