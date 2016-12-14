import random
from extended_euclidean import *


def gcd(big, small):
    if small == 0:
        return big
    else:
        return gcd(small, big % small)


def fast_pow(num, fac):
    if fac < 2:
        return num ** fac
    else:
        return fast_pow(num, (fac + 1) / 2) * fast_pow(num, fac / 2)


def compute_rsa_param(prime_p, prime_q):
    n = prime_p * prime_q
    euler_n = (prime_p - 1) * (prime_q - 1)
    encrpt_num = random.randint(2, euler_n - 1)
    while gcd(euler_n, encrpt_num) != 1:
        encrpt_num = random.randint(2, euler_n - 1)
    decrpt_num = ExtendedGcdEuclidean(modulo_num=euler_n, another_num=encrpt_num).get_result()
    return encrpt_num, decrpt_num, n


def encrypt(msg_byte, e, n):
    return fast_pow(msg_byte, e) % n


def decrypt(cipher_byte, d, n):
    return fast_pow(cipher_byte, d) % n


def demo_rsa_cipher(msg_byte):
    print 'msg byte:', msg_byte
    e, d, n = compute_rsa_param(11, 17)
    print 'PU-Key:', e, n
    print 'PR-Key:', d, n
    cipher_byte = encrypt(msg_byte, e, n)
    print 'cipher byte:', cipher_byte
    decrypt_msg_byte = decrypt(cipher_byte, d, n)
    print 'decrypted msg byte:', decrypt_msg_byte


if __name__ == '__main__':
    for i in range(10):
        print fast_pow(2, i)
    msg_byte = random.randint(1, 255)
    demo_rsa_cipher(msg_byte)
