import random
from string import punctuation # provides randomized numbers 

def shuffle(string):
    temptList = list(string)
    random.shuffle(temptList)
    return ''.join(temptList)

#Main Program
uppercaseLetter1 = chr(random.randint(65,90)).upper() # This uses the ASCII code decimals and generates the alphabets of A to Z in capitals. 
uppercaseLetter2 = chr(random.randint(65,90)).upper() # This uses the ASCII code decimals and generates the alphabets of A to Z in capitals.
lowercaseLetter1 = chr(random.randint(97,122)) # This uses the ASCII code decimals for lower cases for the alphabet A and Z
lowercaseLetter2 = chr(random.randint(97,122)) # This uses the ASCII code decimals for lower cases for the alphabet A and Z
digit1 = int(random.randint(48,57)) # This will generate random numbers between 0-9
digit2 = int(random.randint(48,57)) # This will generate random numbers between 0-9
punctuationSign1 = str(random.randint(33,152)) # This will generate random punctuation 
punctuationSign2 = str(random.randint(33,152)) # This will generate random punctuation 

# Create Password using all the characters 
password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + str(digit1) + str(digit2) + punctuationSign1 + punctuationSign2

#output
print(password)
