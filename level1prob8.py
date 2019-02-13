#In Python, a string can be split on a delimiter.
#Input Format 
#The first line contains a string consisting of space separated words.
#
#Output Format 
#Print the formatted string as explained above.
#
#Sample Input
#
#this is a string   
#Sample Output
#
#this-is-a-string
#

################    Solution    #################

def split_and_join(line):
    # write your code here
     return("-".join(line.split(" ")))
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
