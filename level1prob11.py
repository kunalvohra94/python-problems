#Input Format
#
#The first line of input contains the original string. The next line contains the substring.
#
#Constraints
#
#
#Each character in the string is an ascii character.
#
#Output Format
#
#Output the integer number indicating the total number of occurrences of the substring in the original string.
#
#Sample Input
#
#ABCDCDC
#CDC
#Sample Output
#
#2
#
###############  Solution  ################
  
  
  
def count_substring(string, sub_string):
    count = 0
    index = 0

    for i in range(0, len(string)):
        if string[i] == sub_string[0]:
            if string[i:i+len(sub_string)] == sub_string:
                count += 1
    return count

if __name__ == '__main__':
    string = raw_input().strip()
    sub_string = raw_input().strip()
    
    count = count_substring(string, sub_string)
    print count
