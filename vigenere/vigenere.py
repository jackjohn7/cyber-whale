#!/usr/bin/python3

def encrypt_v0_2(src: str, key: str) -> str:
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
            nc = (ord(c)-m_offset + k) % 26 + m_offset # new character
            result += chr(nc)
            char_count += 1
        else:
            # for now, do not alter numbers and symbols
            result += c
    return result

def encrypt(plain_text, key):
    # The cipher variable will store the final encrypted key
    cipher = ""
    # The starting index for the key used begins at 0
    kindex = 0
    for i in plain_text:
        # For each character in the input string need to determine the ascii value of that character stored in temp as it will keep changing
        temp = ord(i)
        
        # After determining the ascii of the text character, the ascii of the current letter of the key is needed saved in ktemp
        ktemp = ord(key[kindex])

        # After obtaining the two indiviual ascii values add the two together to get the ciphered letter 
        # There is a case to handle in which the letter is upper or lower case using an if statment based on the original plaintext letter
        if temp >= 65 and temp <= 90 :
            # This if statment will handle the upper case letters
            # These corrections will allow the alphabet to be handled easier
            ktemp = ktemp - 64
            temp = temp - 64
            
            # After correcting them they can be added together, using modulo incase of overflow
            ctemp = (ktemp + temp) % 26
        
            # Add the previous subtraction back in to have the correct letter
            ctemp = ctemp + 64
            # Convert the ascii back to a letter
            ctemp = chr(ctemp)

            # After the if statments add the new ciphered letter to the current cipher
            cipher = cipher + ctemp

            # Once getting the current key character increment the index for next itteration, with modulo so the index will not go out of bounds
            kindex = (kindex + 1) % len(key)

        if temp >= 97 and temp <= 122 :
            # This if statment will handle the lower case letters
            # These corrections will allow the alphabet to be handled easier
            ktemp = ktemp - 96
            temp = temp - 96
            
            # After correcting them they can be added together, using modulo incase of overflow
            ctemp = (ktemp + temp) % 26
            
            # Add the previous subtraction back in to have the correct letter
            ctemp = ctemp + 96
            # Convert the ascii back to a letter
            ctemp = chr(ctemp)

            # After the if statments add the new ciphered letter to the current cipher
            cipher = cipher + ctemp

            # Once getting the current key character increment the index for next itteration, with modulo so the index will not go out of bounds
            kindex = (kindex + 1) % len(key)

        else:
            # The else is to handle every other character that is not a letter as those should not be changed
            ctemp = chr(temp)
            # After the if statments add the new ciphered letter to the current cipher
            cipher = cipher + ctemp

            # Once getting the current key character increment the index for next itteration, with modulo so the index will not go out of bounds
            kindex = (kindex + 1) % len(key)
    
    # At the end return the finished cipher
    print(cipher)

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
        print(encrypt_v0_2(stdin.read(), args.encrypt))
    elif args.decrypt is not None:
        print("decrypt functionality not yet implemented")


