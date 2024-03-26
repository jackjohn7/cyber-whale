plain_text = input("Input the plain_text: ")
key = input("Input the key: ")

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

encrypt(plain_text, key)