import random
from extended_euclidean import *
from number_util import *


def compute_rsa_param(prime_p, prime_q):
    n = prime_p * prime_q
    euler_n = (prime_p - 1) * (prime_q - 1)
    encrpt_num = random.randint(2, euler_n - 1)
    while gcd(euler_n, encrpt_num) != 1:
        encrpt_num = random.randint(2, euler_n - 1)
    decrpt_num = ExtendedGcdEuclidean(modulo_num=euler_n, another_num=encrpt_num).get_result()
    return encrpt_num, decrpt_num, n


# assume msg_byte < n
def encrypt(msg_byte, e, n):
    return fast_pow(msg_byte, e) % n


def decrypt(cipher_byte, d, n):
    return fast_pow(cipher_byte, d) % n


def demo_rsa_cipher(msg_byte, p, q):
    print 'msg byte:', msg_byte
    e, d, n = compute_rsa_param(prime_p=p, prime_q=q)
    print 'PU-Key:', e, n
    print 'PR-Key:', d, n
    cipher_byte = encrypt(msg_byte, e, n)
    print 'cipher byte:', cipher_byte
    decrypt_msg_byte = decrypt(cipher_byte, d, n)
    print 'decrypted msg byte:', decrypt_msg_byte


if __name__ == '__main__':
    p, q = 11, 17
    msg_byte = random.randint(1, p * q - 1)
    demo_rsa_cipher(msg_byte, p, q)
