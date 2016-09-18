#Crypto Homework Notes
##Euclidean Algorithm For greatest common divider(gcd)
```python
def gcd_euclidean(lhs, rhs):
    if rhs == 0:
        return lhs
    else:
        return gcd_euclidean(rhs, lhs % rhs)
```

##Extended Euclidean Algorithm
- Imlementation:
```python
class ExtendedGcdEuclidean:
    def __init__(self, lhs, rhs):
        self.r_list = list([lhs,rhs])
        self.q_list = list([None,None])
        self.x_list = list([1,0])
        self.y_list = list([0,1])
        self.iter_list = list([-1,0])
        self.is_break = False;
        self.compute_final_result()

    def do_one_iteration(self):
        next_tail_index = len(self.iter_list)
        self.iter_list.append(self.iter_list[next_tail_index - 1] + 1)
        self.q_list.append(self.r_list[next_tail_index - 2] / self.r_list[next_tail_index - 1])
        self.r_list.append(self.r_list[next_tail_index - 2] % self.r_list[next_tail_index - 1])
        if self.r_list[next_tail_index] == 0:
            self.is_break = True
            return
        self.x_list.append(
                self.x_list[next_tail_index - 2] - self.q_list[next_tail_index] * self.x_list[next_tail_index - 1])
        self.y_list.append(
                self.y_list[next_tail_index - 2] - self.q_list[next_tail_index] * self.y_list[next_tail_index - 1])

    def compute_final_result(self):
        while not self.is_break:
            self.do_one_iteration()
```

- Usage:
```python
def test_extended_gcd_eculidean(lhs, rhs):
    extend_euclidean_algo = ExtendedGcdEuclidean(lhs, rhs)
    for i in range(0, len(extend_euclidean_algo.iter_list) - 1):
        print 'iter:' + str(extend_euclidean_algo.iter_list[i]) + '\t\tr:' + str(
                extend_euclidean_algo.r_list[i]) + '\t\tq:' + str(extend_euclidean_algo.q_list[i]) + '\t\tx:' + str(
                extend_euclidean_algo.x_list[i]) + '\t\ty:' + str(extend_euclidean_algo.y_list[i])

    i = len(extend_euclidean_algo.iter_list) - 1
    print 'iter:' + str(extend_euclidean_algo.iter_list[i]) + '\t\tr:' + str(
            extend_euclidean_algo.r_list[i]) + '\t\tq:' + str(extend_euclidean_algo.q_list[i])


test_extended_gcd_eculidean(1759, 550)
print '\n'
test_extended_gcd_eculidean(1137, 29)
```

##Tranposition Cipher & Substitution Cipher
Substitution Cipher, includes a one-to-one mapping-function from the english letters domain to english letters domain. So
it is possible to do some statistical analysis, based on the common frequency distribution of english letters, and in Q2
, we know that 20000 letters are quite enough to conduct such analysis. If we apply this frequency pattern analysis on
the ciphertext, i.e, find a one-to-one mapping-function according to the frequency statistical data, the text which is
encrypted through subsitution cipher should be readable after being decrypted by the mapping function.

Whereas the above frequency analysis methodology does not fit for the crack of transposition cipher, since according to the definition of
transposition cipher, it just simply transpose the whole plaintext without any substitution.

So, in conclusion, if after we apply the above methodology on the 20000-length text, the text becomes much more readable,
 then it is substitution cipher, else it is transposition cipher.

##Q3 Answer
- mapping function
a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z
--- | --- | --- | --- | --- | --- | --- | --- | --- | --- |--- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---
Y | L | X | U | W | Z | C | A | D | E | F | B | G | I | V | H | O | K | R | Q | P | T | N | J | M | S

> a legacy of atmospheric atomic bomb testing is present in an unlikely
place: people's teeth. according to a report published today in the
journal nature, bomb-generated carbon isotopes trapped in tooth enamel
may provide a more precise method for determining a deceased individual's
age than other forensic method scan.

> the above ground nuclear tests that occurred between 1955 and 1963
dramatically increased the amount of the isotope carbon 14 in the
atmosphere. the levels rapidly equalized around the globe, even
though the explosions occurred at only a few locations, and entered
plants in the food chain through photosynthesis. by eatingp lants,
and animals that feed on plants, humans absorb carbon 14 and exhibit
levelsof the benign, traceable isotope that aresimilar toatmospheric
concentrations. whatismore, carbon 14 decays witha half-life of
5,730 years, a phenomenon that scientists can exploit as away to
determine the ages of objects that contain the isotope. for the new
study, jonasfrisen of the medical nobel institute in stockholm,
sweden, and his colleagues analyzed the carbon content of toothe namel.
because teeth do not exhibit any turn over during a person's life,
the scientists can determine when a tooth formed by comparing its
carbon 14 content to past atmospheric levels. in addition, adult
teeth form during a distinct period of childhood development around
age 12, so this information can be translated into the age of an
individual.

##Q4 Substitution Cipher
- Implementation
```python
class EngIndexBimap:
    def __init__(self):
        self.char2index_dict = dict()
        self.index2char_dict = dict()
        for i in range(0, 25):
            self.char2index_dict[chr(ord('a') + i)] = i
            self.index2char_dict[i] = chr(ord('a') + i)

    def char2index(self, ch):
        return self.char2index_dict[ch]

    def index2char(self, index):
        return self.index2char_dict[index]


# val from 0 to 25
def encrpt(letter_index, k0, k1):
    return (letter_index * k0 + k1) % 26


def cipher(msg, k0, k1):
    my_bimpa = EngIndexBimap()
    cipher_text = list()
    for ele in msg:
        cipher_text.append(my_bimpa.index2char(encrpt(my_bimpa.char2index(ele), k0, k1)))
    return cipher_text
```

- Usage
```python
print cipher('lecture',3,1)
```