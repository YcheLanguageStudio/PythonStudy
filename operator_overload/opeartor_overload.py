class FiniteFieldNumber:
    def __init__(self, bin_str):
        self.integer_32bits = int(bin_str, 2)
        self.px_integer_32bits = int(bin_str, 2)

    def __mod__(self, other):
        return 



if __name__=='__main__':
    print