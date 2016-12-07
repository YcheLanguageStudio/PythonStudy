ipad_str = '00110110'
opad_str = '01011100'

import hashlib


class HMAC:
    def __init__(self, secret_key_integer, hash_func):
        secret_key_bin = bin(secret_key_integer)[2:]
        bits_num = len(secret_key_bin) + 7 / 8 * 8
        padding_num = bits_num - len(secret_key_bin)
        secret_key_bin = ''.join(['0' for i in range(padding_num)]) + secret_key_bin

        self.ipad = int(''.join([ipad_str for i in range(bits_num / 8)]), 2)
        self.opad = int(''.join([opad_str for i in range(bits_num / 8)]), 2)
        self.secret_key = int(secret_key_bin, 2)
        self.hash_func = hash_func

    def compute_hmac_value(self, msg_str):
        partial_res = self.hash_func(hex(self.secret_key ^ self.ipad)[2:] + msg_str).hexdigest()
        return self.hash_func(str(self.secret_key ^ self.ipad) + partial_res).hexdigest()


if __name__ == '__main__':
    algorithm = HMAC(3213, hashlib.md5)
    result = algorithm.compute_hmac_value("message")
    print result
