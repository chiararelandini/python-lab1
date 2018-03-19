#EXERCISE 2 – STRING EXPERIMENT
#Given a string, return a string made of the first two and the last two chars of the original
# string. e.g., ‘spring’ yields ‘spng’
#If the string is shorter than two characters, return the empty string.

print("Insert a string")
string = input()

if len(string)<2 :
    print("")

else:
    string_fin = string[0]+string[1]+string[len(string)-2]+string[len(string)-1]
    print(string_fin)