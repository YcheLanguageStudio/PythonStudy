import re


def demo_join():
    yche_str = ['1', '2', '3']
    yche_str.reverse()
    print yche_str

    print '-'.join(yche_str)


def demo_re():
    my_str = 'The Answer is haha'
    if re.match('.*[Aa]nswer.*', my_str):
        print my_str
    else:
        print 'bad'

    print type('1,2,3'.split())


def demo_substr():
    s = '01234'
    print s[0:1]


if __name__ == '__main__':
    demo_join()
    demo_re()
    demo_substr()
