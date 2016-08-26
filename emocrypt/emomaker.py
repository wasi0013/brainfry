#import urllib2
from bs4 import BeautifulSoup
import re
from fractions import gcd
import random


def affine_encrypt(text, a, b, m=26):
    """
    takes string as text and decrypts it with the key a,b
    >>> affine_encrypt("AFFINE CIPHER",5,8)
    'IHHWVC SWFRCP'
    """
    if gcd(a, m) == 1:
        return u"".join(
            i if i == " " else chr((a * (ord(i.lower()) - 97) + b) % m + 65) for i in text if i.isalpha() or i == " ")


def affine_decrypt(text, a, b, m=26):
    """
    takes string as text and decrypts it with the key a,b
    >>> affine_decrypt("IHHWVC SWFRCP",5,8)
    'AFFINE CIPHER'
    """
    coprimes = [i for i in range(1, m) if gcd(m, i) == 1]
    c = None
    for num in coprimes:
        if (num * a) % m == 1:
            c = num
    return u"".join(
        i if i == " " else chr((c * (ord(i.lower()) - 97 - b)) % m + 65) for i in text if i.isalpha() or i == " ")


def emo_maker(emo_list, text):
    """
    returns: unicode-emoji string
    takes a list of emoji and a text string as argument
    encrypts the text as unicode-emoji
    """
    output = u""
    a = random.randint(2, 25)
    while gcd(a, 26) != 1:
        a = random.randint(2, 25)
    b = random.randint(1, 128)
    encrypted_text = affine_encrypt(text, a, b)
    for i in encrypted_text:
        num = ord(i)
        output += emo_list[num]

    return emo_list[a] + emo_list[b] + output


def emo_decode(emo_list, emo_text):
    """
    returns: decrypted text (in Uppercase Letter)
    decrypts the unicode-emoji strings as texts
    """
    #shielding surrogate emoji
    emo_text = emo_text.encode('utf-16', 'surrogatepass').decode('utf-16')
    a = emo_list.index(emo_text[0])
    b = emo_list.index(emo_text[1])
    encrypted_text = ""
    for i in emo_text[2::]:
        encrypted_text += chr(emo_list.index(i))
    return affine_decrypt(encrypted_text, a, b)


def get_emo_list(page):
    """
    emoji parser: collects emoji from the page
    returns: list of unicode-emoji
    """
    soup = BeautifulSoup(page)
    table = soup.find('table')
    # emo_dict= dict()

    emo_list = list()
    for row in table.findAll('tr')[1:]:
        col = row.findAll('td')

        # TODO replace it with better solution
        try:
            # name of the emo
            # text = col[15].get_text()
            # emo_dict[col[3].find("img").get("alt","")] = text
            emo_list.append(col[3].find("img").get("alt", ""))
        except:
            pass

    return emo_list

