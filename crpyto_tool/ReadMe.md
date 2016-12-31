#Crpyto Tool
##Number Theorem
- [Finite Field](libs/finite_field_op.py), finite field implementation, $modulo_poly(x)=x^8 + x^4 + x^3+ x + 1$,
basic operations are provided

##Extended Eculidean Algorithm
- [With Integer](libs/extended_euclidean.py), extended eculidean implementation for integers
- [With Finite Filed](libs/extended_euclidean_poly.py), extended eculidean implementation for finite field numbers

##Chinese Remainder Theorem
- [Chinese RemainderUsage](libs/chinese_remainder_theorem.py), chinese remainder theorem implementation

##Cipher
###Symmetric
- [Substitution Cipher](libs/substitution_cipher.py), a simple substitution cipher

###Public-Key
- [RSA](libs/rsa.py), public-key cipher: rsa
- [RSA-Variant](libs/rsa_with_chinese_remainder.py), public-key cipher: rsa-variant with chinese remainder
- [Elgamal](libs/elgamal.py), public-key cipher: elgamal

##Hash Related
- [HMAC](libs/hmac.py), hmac implementation with `md5` as the hash function
- [SHA-1](libs/sha1.py), components in sha1 implementation

##All Related Tests

All related tests are put in folder [tests](tests)
