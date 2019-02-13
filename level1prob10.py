#Read a given string, change the character at a given index and then print the modified string.
#
#Input Format 
#The first line contains a string, 
#Output Format 
#Using any of the methods explained above, replace the character at index  with character .
#
#Sample Input
#
#abracadabra
#5 k
#Sample Output
#
#abrackdabra
#
####  Solution ####

def mutate_string(string, position, character):
    strlist = list(string)
    strlist[position] = character
    return("".join(strlist))

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
