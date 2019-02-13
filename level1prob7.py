#You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
#
#For Example:
#
#Www.HackerRank.com → wWW.hACKERrANK.COM
#Pythonist 2 → pYTHONIST 2
#Input Format
#
#A single line containing a string .
#
#Constraints
#
#
#Output Format
#
#Print the modified string .
#
#Sample Input 0
#
#HackerRank.com presents "Pythonist 2".
#Sample Output 0
#
#hACKERrANK.COM PRESENTS "pYTHONIST 2".
#

##############################    Solution   #################################


import string

def swap_case(s):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    T = []
    for i in range(len(s)):
        if s[i] in lower:
            T.append(s[i].upper())
        elif s[i] in upper:
            T.append(s[i].lower())
        else:
            T.append(s[i])
    return(''.join(T))

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
