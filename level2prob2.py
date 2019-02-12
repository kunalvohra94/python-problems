#Consider the following:
#
#A string, , of length  where .
#An integer, , where  is a factor of .
#We can split  into  subsegments where each subsegment, , consists of a contiguous block of  characters in . Then, use each  to create string  such that:
#
#The characters in  are a subsequence of the characters in .
#Any repeat occurrence of a character is removed from the string such that each character in  occurs exactly once. In other words, if the character at some index  in  occurs at a previous index  in , then do not include the character in string .
#Given s and k , print n/k lines where each line i denotes sub string.
#
#Sample Input
#
#AABCAAADA
#3   
#Sample Output
#
#AB
#CA
#AD
#Explanation
#
#String  is split into n/k = 9/3 = 3 equal parts of length k =3. 
#We convert each  to  by removing any subsequent occurrences non-distinct characters in :
#
#Like 
#AAB to AB
#CAA to CA
#ADA to AD
#We then print each  on a new line.



#################################   Solution   ######################### 



from collections import OrderedDict
def merge_the_tools(string, k):
    # your code goes here
    lengthofstring = len(string)
    lines = int(lengthofstring/k);
    val = 0
 
    for i in range (0,lines):
        newstr = string[val:val+k]
        print "".join(OrderedDict.fromkeys(newstr))
        val = val + k
if __name__ == '__main__':
    string, k = raw_input(), int(raw_input())
    merge_the_tools(string, k)
