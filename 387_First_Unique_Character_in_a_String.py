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

"""
Time - O(n)
ANOTHER METHOD USING INBUILT collections.Counter and enumerate.
does not affect time complexity 

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        freq = collections.Counter(s)
        
        #collections.Counter will give dictionary of character and count/frequency in descending order
        print(freq) #Counter({'e': 4, 'l': 2, 'o': 2, 'v': 1, 't': 1, 'c': 1, 'd': 1})

        
        #enumerate will give number and character you can start numbering from any number as you wish
        #default will be 0
        print(list(enumerate(s))) #[(0, 'l'), (1, 'o'), (2, 'v'), (3, 'e'), (4, 'l'), (5, 'e'), (6, 'e'), (7, 't'), (8, 'c'), (9, 'o'), (10, 'd'), (11, 'e')]
        
        
        for index,character in enumerate(s):
            if freq[character] == 1:
                return index
        return -1
"""