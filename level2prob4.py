'''
In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools . To read more about this function, Check this out .

You are given a string . Suppose a character '' occurs consecutively  times in the string. Replace these consecutive occurrences of the character '' with  in the string.

For a better understanding of the problem, check the explanation.

Input Format

A single line of input consisting of the string .

Output Format

A single line of output consisting of the modified string.

Constraints

All the characters of  denote integers between  and .


Sample Input

''''

##########   Solution   ################ 


from itertools import groupby

S = str(raw_input())
T = [list(g) for k, g in groupby(S)]

for i in T:
    print (len(i), int(i[0])),
