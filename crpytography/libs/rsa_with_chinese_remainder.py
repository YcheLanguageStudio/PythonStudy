import random
from number_util import *
from chinese_remainder_theorem import *


def compute_rsa_with_crt_param(prime_p, prime_q):
    p_mul_inv = ExtendedGcdEuclidean(modulo_num=prime_q - 1, another_num=prime_p).get_result()
    q_mul_inv = ExtendedGcdEuclidean(modulo_num=prime_p - 1, another_num=prime_q).get_result()
    n = prime_p * prime_q
    return p_mul_inv, q_mul_inv, n


# assume msg_byte < n
def encrypt(msg_byte, n):
    return fast_pow(msg_byte, n) % n


def decrypt(cipher_text_byte, p, p_mul_inv, q, q_mul_inv):
    remainder_list = [fast_pow(cipher_text_byte, p_mul_inv) % q, fast_pow(cipher_text_byte, q_mul_inv) % p]
    prime_list = [q, p]
    return ChineseRemainder(pairwise_prime_nums=prime_list).get_original_number(remainder_lst=remainder_list)


def demo_rsa_with_crt_param(msg_byte, p, q):
    print 'msg byte:', msg_byte
    p_mul_inv, q_mul_inv, n = compute_rsa_with_crt_param(p, q)
    print 'PU-Key:', n
    print 'PR-Key:', p, p_mul_inv, q, q_mul_inv
    cipher_byte = encrypt(msg_byte, n)
    print 'cipher byte:', cipher_byte
    decrypt_msg_byte = decrypt(cipher_byte, p=p, p_mul_inv=p_mul_inv, q=q, q_mul_inv=q_mul_inv)
    print 'decrypted msg byte:', decrypt_msg_byte


if __name__ == '__main__':
    p, q = 11, 17
    msg_byte = random.randint(1, p * q - 1)
    demo_rsa_with_crt_param(msg_byte, p, q)
