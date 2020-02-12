"""
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"

Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"

"""



class Solution:
    def defangIPaddr(self, address: str) -> str:
    #manual method - 
    #create an empty string to store result
        result = ""
        
    # if character is a digit then add it to result 
    # else it must be . so add [.] to result
        for character in address:
            if character.isdigit():
                result += character
            else:
                result += "["
                result += "."
                result += "]"
                
        return result
    
    """
    METHOD 2 - 
        One line solution using replace - O(n)
    
    class Solution:
        def defangIPaddr(self, address: str) -> str:
        
        address = address.replace(".","[.]")
        
        return address
        """
        