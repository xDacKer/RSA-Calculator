#!/usr/bin/env python3

from Crypto.Util.number import long_to_bytes

print(r'''
__/\\\\\\\\\\\\__________________________________/\\\________/\\\______________________________        
 _\/\\\////////\\\_______________________________\/\\\_____/\\\//_______________________________       
  _\/\\\______\//\\\______________________________\/\\\__/\\\//__________________________________      
   _\/\\\_______\/\\\__/\\\\\\\\\________/\\\\\\\\_\/\\\\\\//\\\_________/\\\\\\\\___/\\/\\\\\\\__     
    _\/\\\_______\/\\\_\////////\\\_____/\\\//////__\/\\\//_\//\\\______/\\\/////\\\_\/\\\/////\\\_    
     _\/\\\_______\/\\\___/\\\\\\\\\\___/\\\_________\/\\\____\//\\\____/\\\\\\\\\\\__\/\\\___\///__   
      _\/\\\_______/\\\___/\\\/////\\\__\//\\\________\/\\\_____\//\\\__\//\\///////___\/\\\_________  
       _\/\\\\\\\\\\\\/___\//\\\\\\\\/\\__\///\\\\\\\\_\/\\\______\//\\\__\//\\\\\\\\\\_\/\\\_________ 
        _\////////////______\////////\//_____\////////__\///________\///____\//////////__\///__________
''')

print('             RSA Calculator')
print('________________________________________')
print('| Operations list                      |')
print('| [1] P & Q = N                        |')
print('| [2] P & N = Q                        |')
print('| [3] Totient(N)                       |')
print('| [4] Plaintext, E & N = Ciphertext    |')
print('| [5] Q, P & E = D                     |')
print('| [6] P, Ciphertext, E & N = Plaintext |')
print('|                                      |')
print('| [0] Exit the programm                |')
print('|¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯|')
print('|              EXTRA MODE              |')
print('| [99] Decrypt the picoCTF 2019 flag   |')
print('¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯')

exit = False
while exit == False:
    choice = int(input('Enter the operation number: '))

    if choice == 1:
        p = int(input('Enter p: '))
        q = int(input('Enter q: '))
        result = p * q
        print("The result is:", result)
    elif choice == 2:
        p = int(input('Enter p: '))
        n = int(input('Enter n: '))
        result = n // p
        print("The result is:", result)
    elif choice == 3:
        p = int(input('Enter p: '))
        q = int(input('Enter q: '))
        result = (p - 1) * (q - 1)
        print("The result is:", result)
    elif choice == 4:
        pt = int(input('Enter plaintext: '))
        e = int(input('Enter e: '))
        n = int(input('Enter n: '))
        result = pow(pt, e, n)
        print("The result is:", result)
    elif choice == 5:
        p = int(input('Enter p: '))
        q = int(input('Enter q: '))
        e = int(input('Enter e: '))
        phi = (p - 1) * (q - 1)
        result = pow(e, -1, phi)
        print("The result is:", result)
    elif choice == 6:
        p = int(input('Enter p: '))
        ct = int(input('Enter ciphertext: '))
        e = int(input('Enter e: '))
        n = int(input('Enter n: '))
        q = n // p
        phi = (p - 1) * (q - 1)
        d = pow(e, -1, phi)
        result = pow(ct, d, n)
        print("The result is:", result)
        picoctf2019 = result
    elif choice == 99:
        flag = long_to_bytes(picoctf2019).decode('UTF-8')
        print(flag)
    elif choice == 0:
        exit = True
    else:
        print('Wrong number')
        n = int(input('Enter n: '))
        result = pow(pt, e, n)
        print("The result is:", result)
    elif choice == 5:
        p = int(input('Enter p: '))
        q = int(input('Enter q: '))
        e = int(input('Enter e: '))
        phi = (p - 1) * (q - 1)
        result = pow(e, -1, phi)
        print("The result is:", result)
    elif choice == 6:
        p = int(input('Enter p: '))
        ct = int(input('Enter ciphertext: '))
        e = int(input('Enter e: '))
        n = int(input('Enter n: '))
        q = n // p
        phi = (p - 1) * (q - 1)
        d = pow(e, -1, phi)
        result = pow(ct, d, n)
        print("The result is:", result)        
    elif choice == 0:
        exit = True
    else:
        print('Wrong number')
