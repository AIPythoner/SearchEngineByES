def square_digits(num):
    str_num = str(num)
    list_num = []
    for i in range(len(str_num)):
        list_num.append(int(str_num[i])**2)
    fina_num = ""
    for i in list_num:
        fina_num += str(i)
    return int(fina_num)




def fake_bin(x):
    list_num = list(x)
    for i in range(len(x)):
        if int(x[i]) < 5:
            list_num[i] = "0"
        else:
            list_num[i] = "1"
    return "".join(list_num)


def find_next_square(sq):
    from math import sqrt
    if int(sqrt(sq)) ** 2 != sq:
        return -1
    tag = True

    while tag:
        sq += 1
        if int(sqrt(sq)) ** 2 == sq:
            return sq

def circleArea(r):
    if r < 0 or not isinstance(r,(int,float)):
        return False
    return round(r*r*3.141592653589793, 2)



def series_sum(n):
    list_ = []
    n = 1
    for i in range(n):
        list_.append(n)
        n += 3
    return list_
print(series_sum(3))


def Descending_Order(num):
    list_ = [int(x) for x in list(str(num))]
    for i in range(len(list_)):
        for j in range(len(list_)-i-1):
            if list_[j] < list_[j+1]:
                list_[j], list_[j+1] = list_[j+1],list_[j]
    return int("".join([str(x) for x in list_]))

from string import ascii_lowercase
print(ascii_lowercase)


def maskify(cc):
    if len(cc) < 4:
        return cc
    return #*(len(cc)-4) + cc[(len(cc)-4):]

import itertools
for i in itertools.combinations('ABCD', 3):
    print (''.join(i))

"""
1234   11 12 13 456 1235
"""

def solve(s):  #s = 1341 == 7

    pass



a = "the-stealth-warrior"
b = "The-Stealth-Warrior"
def to_camel_case(text):
    if text == "":
        return ""
    if '-' in text:
        list_s = text.split("-")
        for i in range(1,len(list_s)):
            list_s[i] = list_s[i].capitalize()
        return "".join(list_s)
    if '_' in text:
        list_s = text.split("_")
        for i in range(len(list_s)):
            list_s[i] = list_s[i].capitalize()
        return "".join(list_s)
print(to_camel_case(a))