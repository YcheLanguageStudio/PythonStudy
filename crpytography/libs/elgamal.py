import random
from number_util import *
from extended_euclidean import *


def compute_elgamal_param(primitive_root, prime_q):
    x_a = random.randint(2, prime_q - 2)
    y_a = fast_pow(primitive_root, x_a) % prime_q
    return x_a, y_a


# assume msg_byte < prime_q
def encrypt(msg_byte, primitive_root, prime_q, y_a):
    rand_k = random.randint(1, prime_q - 1)
    secret_key = fast_pow(y_a, rand_k) % prime_q
    cipher_text0 = fast_pow(primitive_root, rand_k) % prime_q
    cipher_text1 = secret_key * msg_byte % prime_q
    return cipher_text0, cipher_text1


def decrypt(cipher_text0, cipher_text1, x_a, prime_q):
    secret_key = fast_pow(cipher_text0, x_a) % prime_q
    k_multiplicative_inverse = ExtendedGcdEuclidean(modulo_num=prime_q, another_num=secret_key).get_result()
    return cipher_text1 * k_multiplicative_inverse % prime_q


def demo_elgamal_cipher(msg_byte, alpha, q):
    print 'original msg:', msg_byte
    x_a, y_a = compute_elgamal_param(alpha, q)
    c_0, c_1 = encrypt(msg_byte, alpha, q, y_a)
    print 'cipher_text:', c_0, c_1
    decrypt_msg_byte = decrypt(c_0, c_1, x_a, q)
    print 'decrypted msg:', decrypt_msg_byte


if __name__ == '__main__':
    alpha, q = 10, 19
    msg_byte = random.randint(1, q - 1)
    demo_elgamal_cipher(msg_byte, alpha, q)
