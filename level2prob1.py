#Kevin and Stuart want to play the 'The Minion Game'.
#
#Game Rules
#
#Both players are given the same string, .
#Both players have to make substrings using the letters of the string .
#Stuart has to make words starting with consonants.
#Kevin has to make words starting with vowels. 
#The game ends when both players have made all possible substrings. 
#
#Scoring
#A player gets +1 point for each occurrence of the substring in the string .
#
#
#For Example:
#String  = BANANA
#Kevin's vowel beginning word = ANA
#Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.
#
#
#Your task is to determine the winner of the game and their score.
#
#Input Format
#
#A single line of input containing the string . 
#Note: The string  will contain only uppercase letters: .
#
#
#Constraints
#0<len(s)<=10^6
#
#Output Format
#
#Print one line: the name of the winner and their score separated by a space.
#
#If the game is a draw, print Draw.
#
#Sample Input
#
#BANANA
#Sample Output
#
#Stuart 12
#Note : 
#Vowels are only defined as . In this problem,  is not considered a vowel.
#

#####################   Solution   #########################


def minion_game(string):
    # your code goes here
    lengthofstring = len(string)
    valsplit = list(string)
    counter = 0
    kevin = 0 
    stuart = 0
    while(counter < lengthofstring):
        if valsplit[counter] == 'A' or valsplit[counter] == 'E' or valsplit[counter] == 'I' or valsplit[counter] == 'O' or valsplit[counter] == 'U':
            valueadd = lengthofstring - counter
            kevin = kevin + valueadd
        else:
            valueadd = lengthofstring - counter
            stuart = stuart + valueadd
        counter = counter + 1
    if kevin < stuart:
        print ("Stuart %s" %stuart)
    elif kevin > stuart:
        print ("Kevin %s" %kevin)
    else:
        print("Draw")

if __name__ == '__main__':
    s = raw_input()
    minion_game(s)
