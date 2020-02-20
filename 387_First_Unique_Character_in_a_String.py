"""
Time - O (n)

problem is to find the first non repeating
character and its index we can do this multiple ways 
one way is to store frequency/number of occurences of each 
character and then iterating over the each character in 
the string and checking if its frequency is 1 and as
we want first non repeating we will break out of loop 
as soon as we find the character with frequency 1 
"""


def firstUniqChar(s):
    freq = {}
    index = -1
    for i in range(0,len(s)):
        if s[i] not in freq:
            freq[s[i]] = 1
        else:
            freq[s[i]] += 1
    print(freq)
        
    for i in range(0,len(s)):
        if freq[s[i]] == 1:
            index = i
            char = s[i]
            break
            
    return (char,index)

s="loaveleetcode"
print(firstUniqChar(s))
        