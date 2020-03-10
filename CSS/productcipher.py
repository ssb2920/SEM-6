# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 23:15:13 2020

@author: Shubham Bhate 
Roll no: 8318
"""

import numpy as np

def matrix(x,y,initial):
    return [[initial for i in range(x)] for j in range(y)]
    

def locindex(c): #get location of each character
    loc=list()
    if c=='J':
        c='I'
    for i ,j in enumerate(my_matrix):
        for k,l in enumerate(j):
            if c==l:
                loc.append(i)
                loc.append(k)
                return loc
            
def encryptplayfair(msg):  #Encryption

    msg=msg.upper()
    msg=msg.replace(" ", "")             
    i=0
    for s in range(0,len(msg)+1,2):
        if s<len(msg)-1:
            if msg[s]==msg[s+1]:
                msg=msg[:s+1]+'X'+msg[s+1:]
    if len(msg)%2!=0:
        msg=msg[:]+'X'
    print("CIPHER TEXT:",end=' ')
    while i<len(msg):
        loc=list()
        loc=locindex(msg[i])
        loc1=list()
        loc1=locindex(msg[i+1])
        if loc[1]==loc1[1]:
            print("{}{}".format(my_matrix[(loc[0]+1)%5][loc[1]],my_matrix[(loc1[0]+1)%5][loc1[1]]),end=' ')
        elif loc[0]==loc1[0]:
            print("{}{}".format(my_matrix[loc[0]][(loc[1]+1)%5],my_matrix[loc1[0]][(loc1[1]+1)%5]),end=' ')  
        else:
            print("{}{}".format(my_matrix[loc[0]][loc1[1]],my_matrix[loc1[0]][loc[1]]),end=' ')    
        i=i+2        


def encrypthill(msg):
    msg = msg.replace(" ", "")
    C = make_key()
    len_check = len(msg) % 2 == 0
    if not len_check:
        msg += "0"
    P = create_matrix_of_integers_from_string(msg)
    msg_len = int(len(msg) / 2)
    encrypted_msg = ""
    for i in range(msg_len):
        row_0 = P[0][i] * C[0][0] + P[1][i] * C[0][1]      
        integer = int(row_0 % 26 + 65)
        encrypted_msg += chr(integer)
        row_1 = P[0][i] * C[1][0] + P[1][i] * C[1][1]
        integer = int(row_1 % 26 + 65)
        encrypted_msg += chr(integer)
    return encrypted_msg


def find_multiplicative_inverse(determinant):
    multiplicative_inverse = -1
    for i in range(26):
        inverse = determinant * i
        if inverse % 26 == 1:
            multiplicative_inverse = i
            break
    return multiplicative_inverse


def make_key():
    determinant = 0
    C = None
    while True:
        cipher = input("Input 4 letter key for hill cipher: ")
        C = create_matrix_of_integers_from_string(cipher)
        determinant = C[0][0] * C[1][1] - C[0][1] * C[1][0]
        determinant = determinant % 26
        inverse_element = find_multiplicative_inverse(determinant)
        if inverse_element == -1:
            print("Determinant is not relatively prime to 26, uninvertible key")
        elif np.amax(C) > 26 and np.amin(C) < 0:
            print("Only a-z characters are accepted")
            print(np.amax(C), np.amin(C))
        else:
            break
    return C

def create_matrix_of_integers_from_string(string):
    integers = [chr_to_int(c) for c in string]
    length = len(integers)
    M = np.zeros((2, int(length / 2)), dtype=np.int32)
    iterator = 0
    for column in range(int(length / 2)):
        for row in range(2):
            M[row][column] = integers[iterator]
            iterator += 1
    return M

def chr_to_int(char):
    char = char.upper()
    integer = ord(char) - 65
    return integer

if __name__ == "__main__":
    msg = input("Enter Message: ")
    encrypted_msg = encrypthill(msg)
    print(encrypted_msg)
    key=input("Enter key for playfair cipher")
    key=key.replace(" ", "")
    key=key.upper()
    result=list()
    for c in key: #storing key
        if c not in result:
            if c=='J':
                result.append('I')
            else:
                result.append(c)
    flag=0
    for i in range(65,91): #storing other character
        if chr(i) not in result:
            if i==73 and chr(74) not in result:
                result.append("I")
                flag=1
            elif flag==0 and i==73 or i==74:
                pass    
            else:
                result.append(chr(i))
    k=0
    my_matrix=matrix(5,5,0) #initialize matrix
    for i in range(0,5): #making matrix
        for j in range(0,5):
            my_matrix[i][j]=result[k]
            k+=1

    encryptplayfair(encrypted_msg)
    
"""
Output:

Enter Message: attack
Input 4 letter key for hill cipher: cdfg
RKMFCO
Enter key for playfair cipher: abcd
CIPHER TEXT: UG LG DN 

"""