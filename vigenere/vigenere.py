#!/usr/bin/python3

def encrypt(src: str, key: str) -> str:
    """
    Using the specified key, encrypt source text using vigenere cipher.

    The if the key contains non-alpha characters, it will fail (for now)
    """
    result = ""
    char_count = 0 # using count instead of index cause non-alpha cause problems
    for c in src:
        if c.isalpha():
            # offset is used so we can treat values as being
            #  characters represented 0-25 rather than raw ascii.
            #  It also makes it easier to treat capital and lowercase
            #  the same.
            m_offset = 65 if c.isupper() else 97
            k = ord(key[char_count % len(key)])
            k_offset = 65 if chr(k).isupper() else 97
            k -= k_offset
            nc = (ord(c) - m_offset + k) % 26 + m_offset # new character
            result += chr(nc)
            char_count += 1
        else:
            # for now, do not alter numbers and symbols
            result += c
    return result

def decrypt(src: str, key: str) -> str:
    """
    Using the specified key, decrypt source text using vigenere cipher.

    The if the key contains non-alpha characters, it will fail (for now)
    """
    result = ""
    char_count = 0 # using count instead of index cause non-alpha cause problems
    for c in src:
            if c.isalpha():
                # offset is used so we can treat values as being
                #  characters represented 0-25 rather than raw ascii.
                #  It also makes it easier to treat capital and lowercase
                #  the same.
                m_offset = 65 if c.isupper() else 97
                k = ord(key[char_count % len(key)])
                k_offset = 65 if chr(k).isupper() else 97
                k -= k_offset
                nc = (ord(c) - m_offset - k + 26) % 26 + m_offset # new decrypted character
                result += chr(nc)
                char_count += 1
            else:
                # for now, do not alter numbers and symbols
                result += c
    return result

if __name__ == "__main__":
    # import these only when using CLI tool
    from sys import stdin
    from argparse import ArgumentParser

    # parse CLI arguments
    parser = ArgumentParser(
        prog='Vigenere Cipher Tool',
        description='Can be used to encrypt or decrypt using the vigenere cipher',
        epilog='Written by Kyle Stewart, Katie Sparr, and Jack Branch'
    )
    mode_group = parser.add_mutually_exclusive_group(required = True)
    mode_group.add_argument('-e', '--encrypt', help='Encrypts STDIN with provided key')
    mode_group.add_argument('-d', '--decrypt', help='Decrypts STDIN with provided key')
    # future autokey mode feature?
    #parser.add_argument('-a', '-autokey', action='store_true')
    args = parser.parse_args()

    if args.encrypt is not None:
        print(encrypt(stdin.read(), args.encrypt))
    elif args.decrypt is not None:
        print(decrypt(stdin.read(), args.decrypt))


