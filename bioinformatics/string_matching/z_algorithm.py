import sys
import time


def extract_z_boxes(P, start=1, max_box_size=sys.maxsize):
    n = len(P)
    boxes = [0] * n
    l, r = -1, -1

    for k in xrange(start, n):
        if k > r:
            i = 0
            while k + i < n and P[i] == P[k + i] and i < max_box_size:
                i += 1
            boxes[k] = i
            if i:
                l = k
                r = k + i - 1
        else:
            kp = k - l
            Z_kp = boxes[kp]
            if Z_kp < r - k + 1:
                boxes[k] = Z_kp
            else:
                i = r + 1
                while i < n and P[i] == P[i - k] and i - k < max_box_size:
                    i += 1
                boxes[k] = i - k
                l = k
                r = i - 1
    return boxes


# The pattern you're searching for is simply prepended to the target text
# and than the z algorithm is run on that concatenation
def search_pattern_str_z(pat, txt):
    PT = pat + txt
    n = len(pat)
    boxes = extract_z_boxes(PT, start=n, max_box_size=n)
    return list(map(lambda x: x[0] - n, filter(lambda x: x[1] >= n, enumerate(boxes))))


def search_pattern_str_naive(pat, txt):
    return filter(lambda i: txt[i:i + len(pat)] == pat, range(len(txt) - len(pat) + 1))


if __name__ == '__main__':
    pat = 'aba'
    txt = 'bbabaxababay'
    print 'naive:', search_pattern_str_naive(pat, txt)
    print 'z algorithm:', search_pattern_str_z(pat, txt)
