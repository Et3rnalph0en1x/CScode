#Lab 7 Q1

#Rajesh Balasamy

#CS177

#main function

def encrypt(key_text, plain_text):

    key = 0

    for i in range(len(key_text)):

        key = key + int(ord(key_text[i]))


#initialize empty lists and results

    asciiPlain = []

    quotients = []

    encryptedText = ''
    
#for loop that calculates and appends to lists
    
    for j in range(len(plain_text)):

        x = int((key + ord(plain_text[j])) / 127)

        quotients.append(x)

        z = chr((key + ord(plain_text[j])) % 127 + 33)

        encryptedText = encryptedText + z

#print results

    print('The encryption key:',key)

    print('The quotients:',quotients)

    print('The encrypted_text:',encryptedText)

    return(key, quotients, encryptedText)

if __name__ == "__main__":

    main()
